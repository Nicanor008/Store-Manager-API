from flask import Flask, abort, request, make_response, jsonify, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from app.api.v1.models.sales import SalesData, sales
from app.api.v1.models.products import products

# sales list
# sale = SalesData().get_sales()


class Sales(Resource):
    @jwt_required
    def get(self):
        """ 
            Obtain and post sales
        """
        return jsonify({
            'Sales': sales
        })

    @jwt_required
    def post(self):
        """create a sale"""
        sales_data = request.get_json()

        if not sales_data:
            return {"message":"fields cannot be empty"}

        # users data entered, stored in variables
        category = sales_data['category']
        product_name = sales_data['product_name']
        quantity = sales_data['quantity']
        price = sales_data['price']
        
        # check if product is available in the products list
        check_product = [product for product in products if product_name == product["product_name"]]

        if len(check_product) == 0:
            return jsonify({"message":"Product not available"})

        # check if sale record is as per the product quantity
        check_product_quantity = [product for product in products if quantity > product["quantity"]]

        if check_product_quantity:
            return jsonify({"message":"Sale Quantity exceeds the product stock"})


        SalesData().save_sale(category, product_name, quantity, price)
        # message to be displayed 
        return jsonify({'response':'New Sale recorded'})


class GetSingleSale(Resource):
    @jwt_required   
    def get(self, salesId):
        """
            Get only a single sale using saleid
            param : Store Owner/admin and store attendant of the specific sale record
        """
        for sale in sales:
            if int(sale['salesId']) == int(salesId):
                return jsonify({"response":sale})
            # how to handle non-int

        return jsonify({"response":"Sale record Not Available"})     