
users = []

class User():
    def save_user(self, email, first_name, last_name, password, role):
        user_id = len(users) + 1
        user = {
            "user_id": user_id,
            "email": email,
            "first_name":first_name,
            "last_name":last_name,
            "password": password,
            "role": role
        }
        users.append(user)
        return user    

    def get_user(self, email):
        """return user"""
        for user in users:
            if user['email'] == email:
                return user
        # pass

    