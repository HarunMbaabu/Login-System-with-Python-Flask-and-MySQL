import unittest
from flask import session
from main import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        with self.app as client:
            # Perform a POST request to the login endpoint with valid credentials
            response = client.post('/pythonlogin/', data=dict(username='testuser', password='testpassword'))
            self.assertEqual(response.status_code, 302)  # expect a redirect response

            # Ensure session variables are set correctly
            with client.session_transaction() as sess:
                self.assertTrue(sess['loggedin'])
                self.assertEqual(sess['username'], 'testuser')

    def test_register(self):
        with self.app as client:
            # Perform a POST request to the registration endpoint with valid form data
            response = client.post('/pythonlogin/register', data=dict(username='newuser', password='newpassword', email='test@example.com'))
            self.assertEqual(response.status_code, 302)  # expect a redirect response

            # Ensure account was successfully registered
            # You can check the database or perform a login request to verify the registration

    def test_home(self):
        with self.app as client:
            # Perform a GET request to the home endpoint without logging in
            response = client.get('/')
            self.assertEqual(response.status_code, 302)  # expect a redirect response

            # Log in the user
            client.post('/pythonlogin/', data=dict(username='testuser', password='testpassword'))

            # Perform a GET request to the home endpoint after logging in
            response = client.get('/')
            self.assertEqual(response.status_code, 200)  # expect a successful response
            self.assertIn(b'Home Page', response.data)  # expect 'Home Page' to be in the response content

    def test_profile(self):
        with self.app as client:
            # Perform a GET request to the profile endpoint without logging in
            response = client.get('/profile')
            self.assertEqual(response.status_code, 302)  # expect a redirect response

            # Log in the user
            client.post('/pythonlogin/', data=dict(username='testuser', password='testpassword'))

            # Perform a GET request to the profile endpoint after logging in
            response = client.get('/profile')
            self.assertEqual(response.status_code, 200)  # expect a successful response
            self.assertIn(b'Profile Page', response.data)  # expect 'Profile Page' to be in the response content


if __name__ == '__main__':
    unittest.main()
