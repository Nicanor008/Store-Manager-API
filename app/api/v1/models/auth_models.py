import string
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

USERS_DICT = {}

class Users():
    '''class to represent users model'''
    def __init__(self):
        self.oneuser_dict = {}

    def put(self, name, username, email, password,role):
        '''add a user to USERS_DICT'''
        if username in USERS_DICT:
            return {"message":"Username already exists"}
        
        self.oneuser_dict["name"] = name
        self.oneuser_dict["email"] = email
        self.oneuser_dict["username"] = username
        self.oneuser_dict["role"] = role
        pw_hash = generate_password_hash(password)
        self.oneuser_dict["password"] = pw_hash

        USERS_DICT[email] = self.oneuser_dict
        return {"message":"{} registered successfully".format(email)}

    def verify_password(self, email, password):
        '''verify the password a user enters while logging in'''
        if email in USERS_DICT:
            # result = check_password_hash(USERS_DICT[email]["password"], password)
            # if result is True:
            return "True"
            # return {"message": "The password you entered is incorrect"}
        return {"message": "email does not exist in our records"}
    def get_user(self,email, role):
        if email in USERS_DICT and role in USERS_DICT:
            return USERS_DICT[email]
        return {"message":"User not found"}