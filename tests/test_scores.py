from tests.helpers import app


class TestScoresResource(app.AppTestCase):
    def test_can_create(self):
        req = self.app.post_json(
            '/scores',
            {
                'username': 'test',
                'company': 'test',
                'score': 100
            }
        )

        self.assertEqual(req.status_code, 201)
        self.assertEqual(req.json.get('id'), 1)

    def test_can_list(self):
        post_req = self.app.post_json(
            '/scores',
            {
                'username': 'my_user',
                'company': 'test',
                'score': 50
            }
        )
        self.assertEqual(post_req.status_code, 201)

        get_req = self.app.get('/scores')
        self.assertEqual(get_req.status_code, 200)

        score_list = get_req.json.get('scores')
        self.assertEqual(len(score_list), 1)
