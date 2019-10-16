from app import app
import os
import tempfile
import unittest


class BasicTest(unittest.TestCase):
    def test_index(self):
        test_app = app.test_client(self)
        response = test_app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

    def test_database_connection(self):
        test_db = os.path.exists('flasktdd.db')
        self.assertTrue(test_db)


class AppTestCase(unittest.TestCase):
    def setUp(self):
        """temp database to be used to run tests"""
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
        app.create_database()
    
    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

if __name__ == "__main__":
    unittest.main()