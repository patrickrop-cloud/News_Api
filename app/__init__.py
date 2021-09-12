from flask import Flask
from flask_bootstrap import Bootstrap, bootstrap_find_resource
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)

    #Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting config
    from .requests import configure_request
    configure_request(app)

    #will add views and forms
    return app

