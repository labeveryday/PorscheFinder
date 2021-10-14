import unittest
import sys
sys.path.append('./')
import cars

class TestCars(unittest.TestCase):
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
    
    def test_remove_dupes(self):
        """Test remove dupes function"""
        car_list = [
            {
                'datelisted': '2021-10-14 05:48',
                'location': 'atlanta',
                'price': '$17,500',
                'title': '1988 Porsche 944 turbo',
                'url': 'test'
            },
            {
                'location': 'atlanta',
                'price': '$27,800',
                'title': '1986 Porsche 944 Turbo  951 Model Grand Prix White Coupe without '
                         'the h',
                'url': 'test'
            },
            {
                'location': 'atlanta',
                'price': '$17,500',
                'title': '1988 Porsche 944 turbo',
                'url': 'test'
                }
                ]
        results = [
            {
                'datelisted': '2021-10-14 05:48',
                'location': 'atlanta',
                'price': '$17,500',
                'title': '1988 Porsche 944 turbo',
                'url': 'test'
            },
            {
                'location': 'atlanta',
                'price': '$27,800',
                'title': '1986 Porsche 944 Turbo  951 Model Grand Prix White Coupe without '
                         'the h',
                'url': 'test'
            }
        ]
        search = cars.remove_dupes(car_list)
        self.assertEqual(search, results)

if __name__ == "__main__":
    unittest.main(verbosity=2)
