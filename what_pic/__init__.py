from flask import Flask
#import some plugin-apps
from flask.ext.bootstrap import Bootstrap
from config import config


# initiate plugins

bootstrap = Bootstrap()


def create_app(config_name):
    """create a app under specified configuration.

    Args:
        config_name: name of specified configuration
    Return:
        The app
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # some plugins initiations.
    bootstrap.init_app(app)

    # routings from blueprint.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
