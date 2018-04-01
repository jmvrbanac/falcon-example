import uuid


def set_context(req, resp):
    if not req.context.get('request_id'):
        req.context['request_id'] = str(uuid.uuid4())

    resp.set_header('request-id', req.context['request_id'])


class ContextMiddleware(object):
    def process_request(self, req, resp):
        set_context(req, resp)
