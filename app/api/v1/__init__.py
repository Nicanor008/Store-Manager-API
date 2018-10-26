from flask import Flask, Blueprint
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import app_config
from app.api.v1.views.views import Products, GetSingleProduct
from app.api.v1.views.sales import Sales, GetSingleSale
from app.api.v1.views.users import Register, Login

# obtain the blueprint by initialising
version1 = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(version1)



# specific endpoints
api.add_resource(Sales, '/sales')
api.add_resource(GetSingleSale, '/sales/<salesId>')
api.add_resource(Products, '/products')
api.add_resource(GetSingleProduct, '/products/<productId>')
api.add_resource(Register, '/auth/register')
api.add_resource(Login, '/auth/login')
# api.add_resource(Logout, '/auth/logout')
