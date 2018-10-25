import re
from datetime import datetime, timedelta
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
from app.api.v1.models.users import User, users

# The required format of an email-address
email_format = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"

# Users data list
user = User()

class Login(Resource, User):
    """API endpoint to login the registered users
    Returns jsonify users data
    """
    def post(self):
        data = request.get_json()
        
        email = data.get("email")
        password =data.get("password")
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        role = data.get("role")

        if not data:
            response =  jsonify({"message":"Fields cannot be empty"})
        elif not email:
            response =  jsonify({"message":"Email cannot be blank"})
        elif not password:
            response =  jsonify({"message":"Password field cannot be blank"})


            
        if not re.match(email_format, email):
            response = jsonify({"message": "Invalid Email address"})  

        user_exists = [user for user in users if email == user["email"]]

        if not user_exists:
            return jsonify({
                "message":"User does not exist"
            })
        if password != user_exists[0]["password"]:
            return jsonify({
                "message":"Wrong password",
                "status": 400
            })
        
        
        access_token = create_access_token(identity=email)
        # expires = datetime.utcnow() + timedelta(minutes=60)
        response = jsonify(token = access_token, message = "Login successful!")

        return response
        
   

class Register(Resource, User):
    """Admin to register users
        Returns jsonify users data accordingly
    """
    def post(self):
        data = request.get_json()

        email = data.get("email")
        password =data.get("password")
        role = data.get("role")  
        name = data.get("name")     

        if not data:
            return jsonify("Data must be in json format")
        if not email or not password:
            return jsonify({"message":"You must provide email and password"})

        if not re.match(email_format, email):
            return jsonify({"message": "Invalid email address"})        

        user_exists = [user for user in users if email == user["email"]]

        if user_exists:
            return jsonify({"message":"Email address already exists"})

        else:
            User.save_user(self, email,name, password, role)
            # user.save_user(email,name, password, role)
            return jsonify({
                "message":"User has been registered successfully"
            })