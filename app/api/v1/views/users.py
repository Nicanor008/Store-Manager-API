import re
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
from ..models import users

users_list = users.Users()


class Login(Resource):
    """login in registered users     
    Returns:
        token and confirmation message 
    """
    def post(self):
        data = request.get_json()
        if not data:
            return jsonify({"message": "Email and password required"})

        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        # if email is not user
        # if email is not users_list.user_verify
        if not email or not password:
            return jsonify({"message": "Username or password missing"})

        authorize = users_list.user_verify(email, password)
        user=users_list.get_user(email, role)

        if not authorize:
            return "failed"

        access_token = create_access_token(identity=user)
        return jsonify(token = access_token, message = "Login successful!")
        # else:
            # return "failed"
        
        
        
class Register(Resource):
    """
        register new users 
        Returns:
            users data in a list
    """
    def post(self):
        data = request.get_json()

        # users input
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        # confirm_password = data['confirm_password']
        role=data.get('role')

        roles=["owner","admin","attendant"]
        
        if role not in roles:
            return jsonify({"message":"The role {} does not exist".format(role)})
       
        # email format
        email_format = re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        # check if email is a valid 
        if email_format is None:
            return jsonify({"message": "invalid email address"})

        # if password is not confirm_password:
            # return jsonify({'message':'passwords do not match'})

        response = jsonify(users_list.put(name, username, email, password,role))
        response.status_code = 201
        return response

