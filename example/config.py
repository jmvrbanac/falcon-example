from aumbry import Attr, YamlConfig


class DatabaseConfig(YamlConfig):
    __mapping__ = {
        'connection': Attr('connection', str, required=True),
    }

    connection = ''


class AppConfig(YamlConfig):
    __mapping__ = {
        'db': Attr('db', DatabaseConfig, required=True),
        'gunicorn': Attr('gunicorn', dict, required=True),
    }

    def __init__(self):
        self.db = DatabaseConfig()
        self.gunicorn = {}
