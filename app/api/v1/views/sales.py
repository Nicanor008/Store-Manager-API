from flask import Flask, abort, request, make_response, jsonify, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import (JWTManager, jwt_required, get_jwt_claims)
from app.api.v1.models.sales import SalesData

# sales list
sale = SalesData().get_sales()


class Sales(Resource):
    @jwt_required
    def get(self):
        """ 
            Obtain and post sales
        """
        return jsonify({
            'Sales': sale
        })

    @jwt_required
    def post(self):
        """create a sale"""
        sales_data = request.get_json()

        # users data entered, stored in variables
        sales_id = sales_data['salesId']
        category = sales_data['category']
        sale_name = sales_data['product_name']
        quantity = sales_data['quantity']
        price = sales_data['price']
        
        # check if product is available in the products list

        # store products in a dictionary
        sales_cart = {
            "salesId":sales_id, 
            "category":category, 
            "product_name":sale_name, 
            "quantity":quantity,
            "price":price
        }
        # add sale product to the sale list
        sale.append(sales_cart)

        # message to be displayed 
        return jsonify({'response':'New Sale recorded'})


class GetSingleSale(Resource):
    @jwt_required   
    def get(self, salesId):
        """
            Get only a single sale using saleid
            param : Store Owner/admin and store attendant of the specific sale record
        """
        for sales in sale:
            if sales['salesId'] == salesId:
                return jsonify({"response":sales})

        return jsonify({"response":"Product Not Available"})     