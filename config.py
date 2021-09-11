import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=apple&from=2021-09-10&to=2021-09-10&sortBy=popularity&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}