from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import app_config
from app.api.v1.views.views import Products, GetSingleProduct
from app.api.v1.views.sales import Sales, GetSingleSale
from app.api.v1.views.users import auth

# obtain the blueprint by initialising
sales = Blueprint('sales', __name__, url_prefix='/api/v1')
api = Api(sales)

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config['development'])
    
    # register the blueprint
    app.register_blueprint(sales)

    # specific endpoints
    api.add_resource(Sales, '/sales')
    api.add_resource(GetSingleSale, '/sales/<salesId>')
    api.add_resource(Products, '/products')
    api.add_resource(GetSingleProduct, '/products/<productId>')
    

    return app