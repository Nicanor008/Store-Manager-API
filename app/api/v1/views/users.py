import re
import datetime
from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_raw_jwt)
from app.api.v1.models.users import User, users

# The required format of an email-address
email_format = r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)"

# Users data list
user = User()

# blacklist = set()

class Login(Resource, User):
    """API endpoint to login the registered users
    Returns jsonify users data
    """
    def post(self):
        data = request.get_json()
        
        email = data.get("email")
        password =data.get("password")
        # role = data.get("role")

        user_exists = [user for user in users if email == user["email"]]

        if not data:
            response =  jsonify({"message":"Fields cannot be empty"})
        elif not email:
            response =  jsonify({"message":"Email cannot be blank"})
        elif not password:
            response =  jsonify({"message":"Password field cannot be blank"})
        elif not re.match(email_format, email):
            response = jsonify({"message": "Invalid Email address"})  
        elif not user_exists:
            response = jsonify({
                "message":"Wrong email address"
            })
        elif password != user_exists[0]["password"]:
            response =  jsonify({
                "message":"Wrong password"
            })
        else:
            current_user = user.get_user(email)
            expires = datetime.timedelta(minutes=60)
            access_token = create_access_token(identity=current_user, expires_delta=expires)
            response = jsonify(token=access_token, message="Login successful!")

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
        first_name = data.get("first_name")  
        last_name = data.get("last_name")     

        user_exists = [user for user in users if email == user["email"]]

        if not data:
            response =  jsonify({"message":"Fields cannot be empty"})
        elif not email:
            response =  jsonify({"message":"Email cannot be blank"})
        elif not password:
            response =  jsonify({"message":"Password field cannot be blank"})
        elif not first_name:
            response =  jsonify({"message":"first name cannot be blank"})
        elif not role:
            response =  jsonify({"message":"Role cannot be blank"})
        elif not re.match(email_format, email):
            response = jsonify({"message": "Invalid email address"})        
        elif user_exists:
            response = jsonify({"message":"User already exists"})
        else:
            User.save_user(self, email,first_name, last_name, password, role)
            # user.save_user(email,name, password, role)
            response = jsonify({
                "message":"User has been registered successfully"
            })
        return response


# class Logout(Resource):
#     @jwt_required
#     def delete(self):
#         jti = get_raw_jwt()['jti']
#         blacklist.add(jti)
#         return jsonify({"message": "Successfully logged out"}), 200


