from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import app_config
# from app.api.v1.views.users import BLACKLIST


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    
    from app.api.v1 import version1 as v1

    # register the blueprint
    app.register_blueprint(v1)

    app.config['JWT_SECRET_KEY'] = 'thisismysecretkey'
    jwt = JWTManager(app)


    return app