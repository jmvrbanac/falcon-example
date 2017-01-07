import os
import json


def load_schema(name):
    module_path = os.path.dirname(__file__)
    path = os.path.join(module_path, '{}.json'.format(name))

    with open(os.path.abspath(path), 'r') as fp:
        data = fp.read()

    return json.loads(data)
