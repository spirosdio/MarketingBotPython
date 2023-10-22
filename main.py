from user_database import UserDatabase, User

if __name__ == "__main__":
    db = UserDatabase()
    db.create_user('spiros', 'diochnos', 1, '26')
    db.create_user('vaso', 'kollia', 2, '27')
    db.create_user('angelos', 'todri', 3, '28')
