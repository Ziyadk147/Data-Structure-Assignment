import unittest
from selection import selectionSort

class TestMultiLevelSort(unittest.TestCase):
    def test_multi_level_sort(self):
        data = [
            {'First Name': 'Hamza', 'Last Name': 'Farooqui'},
            {'First Name': 'Mohammad', 'Last Name': 'Ali'},
            {'First Name': 'Hamza', 'Last Name': 'Ali'},
            {'First Name': 'Armaan', 'Last Name': 'Sheikh'}
        ]
        
        expected_output = [
            {'First Name': 'Armaan', 'Last Name': 'Sheikh'},
            {'First Name': 'Hamza', 'Last Name': 'Ali'},
            {'First Name': 'Hamza', 'Last Name': 'Farooqui'},
            {'First Name': 'Mohammad', 'Last Name': 'Ali'}
        ]
        
        sorted_data = selectionSort(data, ['First Name', 'Last Name'])
        self.assertEqual(sorted_data, expected_output)
