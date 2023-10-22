import unittest
from user_database import User, UserDatabase

class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        self.db = UserDatabase()
        self.db.create_user("John", "Doe", "123", "30")

    def test_create_user(self):
        user = self.db.get_user("123")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "John")
        self.assertEqual(user.surname, "Doe")
        self.assertEqual(user.age, "30")

    def test_create_duplicate_user(self):
        result = self.db.create_user("Jane", "Doe", "123", "25")
        self.assertEqual(result, None)

    def test_get_user(self):
        user = self.db.get_user("123")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "John")
        self.assertEqual(user.surname, "Doe")
        self.assertEqual(user.age, "30")

    def test_get_nonexistent_user(self):
        user = self.db.get_user("999")
        self.assertIsNone(user)

    def test_list_users(self):
        self.db.create_user("Jane", "Smith", "456", "25")
        users = self.db.get_all_users()
        self.assertEqual(len(users), 2)


if __name__ == '__main__':
    unittest.main()
