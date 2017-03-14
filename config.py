import datetime

class Config(object):

    def init_app(self):
        pass



class DevelopmentConfig(Config):

    UDP_REC_PORT = 10010
    UDP_SND_PORT = 10011
    REDIS_PORT = 6379
    REDIS_DB = 0
    REDIS_REQ_QUEUE = 'reqlist'
    REDIS_ACK_QUEUE = 'acklist'
    REDIS_SND_QUEUE = 'sndlist'
    MYSQL_PORT = 3306
    MYSQL_USER = 'root'
    MYSQL_PASSWD = 'welcome'
    MYSQL_DB = 'devdb'
    MYSQL_LOG_TAB = 'log_{0.year}_{0.month:02d}_{0.day:02d}'.format(datetime.datetime.now())


class ProductConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductConfig,

    'default': DevelopmentConfig
}

RUN_LEVEL = 'development'