import unittest
from city_functions import address

class TestCityName(unittest.TestCase):
    
    def test_city_country(self):
        full_address = address('Santiago', 'Chile')
        self.assertEqual(full_address, 'Santiago Chile')

    def test_city_country_population(self):
        full_address = address('santiago', 'chile', '5000000')
        self.assertEqual(full_address, 'Santiago Chile- Population 5000000')
    
    
if __name__ == '__main__':
    unittest.main()