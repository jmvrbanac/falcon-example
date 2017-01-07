import aumbry


class DatabaseConfig(aumbry.YamlConfig):
    __mapping__ = {
        'connection': ['connection', str],
    }

    connection = ''


class AppConfig(aumbry.YamlConfig):
    __mapping__ = {
        'db': ['db', DatabaseConfig],
        'gunicorn': ['gunicorn', dict],
    }

    db = DatabaseConfig()
    gunicorn = {}
