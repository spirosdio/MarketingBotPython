class User:
    def __init__(self, name, surname, user_id, age):
        self.name = name
        self.surname = surname
        self.user_id = user_id
        self.age = age


class UserDatabase:
    def __init__(self):
        self.users = {}

    def create_user(self, name, surname, user_id, age):
        if user_id not in self.users:
            new_user = User(name, surname, user_id, age)
            self.users[user_id] = new_user
            print(f"User {name} {surname} added with ID {user_id}")
        else:
            print(f"User with ID {user_id} already exists.")

    def get_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return list(self.users.values())

    def list_users(self):
        for user_id, user in self.users.items():
            print(
                f"ID: {user_id}, Name: {user.name}, Surname: {user.surname}, Age: {user.age}")
