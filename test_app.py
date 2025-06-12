import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

if __name__ == "__main__":
    unittest.main()
