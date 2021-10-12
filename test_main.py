import unittest
from main import get_porsche, get_soup

class TestMain(unittest.TestCase):
    """This is to test the Porsche Finder"""
    
    def test_get_porsche_response(self):
        """Send an API request to test connectivity."""
        response = get_porsche()
        self.assertTrue(response)


if __name__ == "__main__":
    unittest.main(verbosity=2)
