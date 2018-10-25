from flask import Flask, abort, request, make_response, jsonify, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from app.api.v1.models.products import ProductsData, products
   

class Products(Resource):
    @jwt_required
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

    @jwt_required
    def post(self):
        """post a product to list
            param: admin only
            return : json single product confirmation
        """
        # fetch users input data
        data = request.get_json()
        if not data:
            return jsonify({"response": "Fields cannot be empty"}) 
        
        category = data.get('category')
        product_name = data.get('product_name')
        quantity = data.get("quantity")
        price = data.get('price')

        ProductsData().save_product(category, product_name, quantity, price)
        # message to be displayed to the user
        return jsonify( {'response':'New product added successfully'})
    
class GetSingleProduct(Resource):
    ''' fetch a single product '''
    @jwt_required
    def get(self, productId):
        """Fetch a single product record
            param:
            <int:productId>
        """
        for product in products:
            if product['productId'] == int(productId):
                return jsonify(
                    {
                        'response':product
                    }
                )
                # handling  string id
        return jsonify({'response':'Product Not Available'})

            