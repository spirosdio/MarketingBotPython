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

    def list_users(self):
        for user_id, user in self.users.items():
            print(f"ID: {user_id}, Name: {user.name}, Surname: {user.surname}, Age: {user.age}")

if __name__ == "__main__":
    db = UserDatabase()

    while True:
        print("\nUser Database Menu:")
        print("1. Create User")
        print("2. Get User")
        print("3. List Users")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            user_id = input("Enter ID: ")
            age = input("Enter age: ")
            db.create_user(name, surname, user_id, age)
        elif choice == '2':
            user_id = input("Enter user ID to get: ")
            user = db.get_user(user_id)
            if user:
                print(f"User found - Name: {user.name}, Surname: {user.surname}, Age: {user.age}")
            else:
                print(f"User with ID {user_id} not found.")
        elif choice == '3':
            db.list_users()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
