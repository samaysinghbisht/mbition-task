import unittest
from flask import Flask
from app import app


class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the mBition Interview Task', response.data)
        self.assertIn(b'This page serves as the starting point for the interview task.', response.data)
        self.assertIn(b'Please add an endpoint to the URL /user-list to see the list of users', response.data)
        print("Test1 Pass")

    def test_user_list(self):
        response = self.app.get('/user-list')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'ID', response.data)
        self.assertIn(b'Name', response.data)
        self.assertIn(b'Email', response.data)
        print("Test2 Pass")

if __name__ == '__main__':
    unittest.main()
