from flask import Flask, abort, request, make_response, jsonify, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from app.api.v1.models.products import ProductsData

# Products lists
products=ProductsData().get_products()
   

class Products(Resource):
    def get(self):
        """Fetch all products
            :param - store attendant and store owner
            Returns: json products
        """
        return make_response(jsonify(
            {
                'Products':products
            }
        ),200)


    def post(self):
        """post a product to list
            param: admin only
            return : json single product confirmation
        """
        # fetch users input data
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"}) 
        id = data['productId']
        category = data['category']
        name = data['name']

        # dictionary data structure for users products
        users_products = {
            "productId":id,
            "category":category,
            "name":name
        }
        # Store products obtained from the user in a list
        products.append(users_products)

        # message to be displayed to the user
        return jsonify( {'response':'New product added successfully'})
    
class GetSingleProduct(Resource):
    ''' fetch a single product '''
    def get(self, productId):
        """Fetch a single product record
            param:
            <int:productId>
        """
        for product in products:
            if product['productId'] == productId:
                return jsonify(
                    {
                        'response':product
                    }
                )
        return jsonify({'response':'Product Not Available'})

            