import string
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash

# users_data = {}

class Users():
    '''class to represent users model'''
    def __init__(self):
        self.user = {} # single user
        self.users_data = {}

    def put(self, name, username, email, password,role):
        '''add a user to users_data'''
        if username in self.users_data:
            return {"message":"Username already exists"}
        
        self.user["name"] = name
        self.user["email"] = email
        self.user["username"] = username
        self.user["role"] = role
        pw_hash = generate_password_hash(password)
        self.user["password"] = pw_hash

        self.users_data[email] = self.user
        return {"message":"{} registered successfully".format(email)}

    def user_verify(self, email, password):
        '''verify the password a user enters while logging in'''
        if email in self.users_data:
            result = check_password_hash(self.users_data[email]["password"], password)
            if result is True:
                return "True"
            return {"message": "The password you entered is incorrect"}
        return {"message": "email does not exist in our records"}
    def get_user(self,email, role):
        if email in self.users_data and role in self.users_data:
            return self.users_data[email]
        return {"message":"User not found"}