import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

SAModel = declarative_base()


class UserScores(SAModel):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(128), unique=True)
    company = sa.Column(sa.String(128))
    score = sa.Column(sa.Integer)

    def __init__(self, username, company, score):
        self.username = username
        self.company = company
        self.score = score

    @property
    def as_dict(self):
        return {
            'username': self.username,
            'company': self.company,
            'score': self.score
        }

    def save(self, session):
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls, session):
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()

        return models
