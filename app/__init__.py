from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import app_config
# from app.api.v1.views.users import BLACKLIST, Login
# from app.api.v1.models.users import User


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    # app.config['JWT_BLACKLIST_ENABLED'] = True
    # app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']

    from app.api.v1 import version1 as v1

    # register the blueprint
    app.register_blueprint(v1)

    app.config['JWT_SECRET_KEY'] = 'thisismysecretkey'
    jwt = JWTManager(app)

    @jwt.user_claims_loader
    def add_claims_to_access_token(user):
        return {'role':user['role']}

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user['email']

    

    # # token attempts to access an endpoint
    @jwt.expired_token_loader
    def my_expired_token_callback():
        return jsonify({
            'message': 'The token has expired'
        }), 401

    return app

