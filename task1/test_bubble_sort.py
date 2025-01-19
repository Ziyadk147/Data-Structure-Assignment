import unittest

from Bubblesort import bubbleSort  

class TestBubbleSort(unittest.TestCase):
    def test_sort_by_transaction_amount(self):
        elements = [
            {'name': 'Hamza', 'transaction_amount': 1000, 'device': 'iphone-10'},
            {'name': 'Hasnain', 'transaction_amount': 400, 'device': 'google pixel'},
            {'name': 'Palwasha', 'transaction_amount': 200, 'device': 'vivo'},
            {'name': 'Aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
        ]
        expected = [
            {'name': 'Palwasha', 'transaction_amount': 200, 'device': 'vivo'},
            {'name': 'Hasnain', 'transaction_amount': 400, 'device': 'google pixel'},
            {'name': 'Aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
            {'name': 'Hamza', 'transaction_amount': 1000, 'device': 'iphone-10'},
        ]
        bubbleSort(elements, "transaction_amount")
        self.assertEqual(elements, expected)

    def test_sort_by_name(self):
        elements = [
            {'name': 'Hamza', 'transaction_amount': 1000, 'device': 'iphone-10'},
            {'name': 'Hasnain', 'transaction_amount': 400, 'device': 'google pixel'},
            {'name': 'Palwasha', 'transaction_amount': 200, 'device': 'vivo'},
            {'name': 'Aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
        ]
        expected = [
            {'name': 'Aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
            {'name': 'Hamza', 'transaction_amount': 1000, 'device': 'iphone-10'},
            {'name': 'Hasnain', 'transaction_amount': 400, 'device': 'google pixel'},
            {'name': 'Palwasha', 'transaction_amount': 200, 'device': 'vivo'},
        ]
        bubbleSort(elements, "name")
        self.assertEqual(elements, expected)

if __name__ == "__main__":
    unittest.main()
