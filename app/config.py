import os


class Config:
    #because of wtf forms 
    SECRET_KEY = os.urandom(32) # generate random key -> length 32
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://new_user_flask:1397@localhost:5432/final_flask'
    UPLOADED_PHOTOS_DEST = 'app/static/'


config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}