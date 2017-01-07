import falcon
import json
import jsonschema


class BaseResource(object):
    def __init__(self, db_manager):
        self.db = db_manager

    def format_body(self, data):
        return json.dumps(data)


def validate(schema):
    def decorator(func):
        def wrapper(self, req, resp, *args, **kwargs):
            try:
                raw_json = req.stream.read()
                obj = json.loads(raw_json.decode('utf-8'))
            except Exception:
                raise falcon.HTTPBadRequest(
                    'Invalid data',
                    'Could not properly parse the provided data as JSON'
                )

            try:
                jsonschema.validate(obj, schema)
            except jsonschema.ValidationError as e:
                raise falcon.HTTPBadRequest(
                    'Failed data validation',
                    e.message
                )

            return func(self, req, resp, *args, parsed=obj, **kwargs)
        return wrapper
    return decorator
