class DBConfig(object):
    def __init__(self, dialect='postgresql', username='postgres', password='1103', host='localhost', port='5432', database='crypto_db'):
        self.dialect = dialect
        self.username = username
        self.password = password
        self. host = host
        self.port = port
        self.database = database

    def get_uri(self):
        # uri = "postgresql://<username>:<password>@localhost:5432/backupdata".format(self.dialect, self.username, self.password, self.host, self.port, self.database)
        uri = "{}://{}:{}@{}:{}/{}".format(self.dialect,
                                           self.username,
                                           self.password,
                                           self.host,
                                           self.port,
                                           self.database)
        return uri

class ModelConfig(object):
    def __init__(self, window_size=360):
        self.window_size = window_size
