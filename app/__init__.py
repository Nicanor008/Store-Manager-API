from flask import Flask
from flask_restful import Api
# from flask_jwt_extended import JWTManager
from instance.config import app_config


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    
    from app.api.v1 import version1 as v1

    # register the blueprint
    app.register_blueprint(v1)

    return app