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
        if products == []:
            return jsonify({'message':'No Products available'})
        else:
            return make_response(jsonify(
                {
                    'message':products
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
            response = jsonify({"response": "Fields cannot be empty"}) 
        
        category = data.get('category')
        product_name = data.get('product_name')
        quantity = data.get("quantity")
        price = data.get('price')

        ProductsData().save_product(category, product_name, quantity, price)
        # message to be displayed to the user
        response = jsonify( {'message':'New product added successfully'})

        return response
    
class GetSingleProduct(Resource):
    ''' fetch a single product '''
    @jwt_required
    def get(self, productId):
        """Fetch a single product record
            param:
            <int:productId>
        """
        try:
            isinstance(int(productId), int)
            for product in products:
                if product['productId'] == int(productId):
                   return jsonify(
                        {
                            'response':product
                        }
                    )
        except ValueError:
            response = jsonify({'message':'Product ID should be an integer'})
            return response
                # handling  string id
        response = jsonify({'response':'Product Not Available'})
        return response



            