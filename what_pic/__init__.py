from flask import Flask
#import some plugin-apps
from config import config


# initiate plugins



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

    # routings from blueprint.
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
