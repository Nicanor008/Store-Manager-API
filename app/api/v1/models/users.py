users = []

class User():
    def save_user(self, email, name, password, role):
        user_id = len(users) + 1
        user = {
            "user_id": user_id,
            "email": email,
            "name":name,
            "password": password,
            "role": role
        }
        users.append(user)
        return user    