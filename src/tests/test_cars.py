import unittest
import sys
sys.path.append('./')
import cars

class TestMain(unittest.TestCase):
    """This is to test the Porsche Finder"""
    
    def test_get_porsche_response(self):
        """Send an API request to test connectivity."""
        response = cars.get_porsche()
        self.assertTrue(response)
    
    def test_build_search(self):
        """Test if path"""
        search = cars.build_search("porsche")
        self.assertEqual(search, "porsche")
    
    def test_build_search_else(self):
        """Test verify else path"""
        search = cars.build_search("porsche 1990 944")
        self.assertEqual(search, "porsche%201990%20944")


if __name__ == "__main__":
    unittest.main(verbosity=2)
