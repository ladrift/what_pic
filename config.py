import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # some global configure variables
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    UPLOAD_FOLDER = os.path.join(basedir, 'what_pic/static/uploads')


    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
