
import unittest

from original_app import process_data as original_process
from optimized_app import process_data as optimized_process


class PerformanceTests(unittest.TestCase):

    def setUp(self):
        self.data = [
            {
                "id": 1,
                "category": "Books",
                "price": 200,
                "quantity": 2
            },
            {
                "id": 2,
                "category": "Food",
                "price": 100,
                "quantity": 5
            },
            {
                "id": 3,
                "category": "Books",
                "price": 300,
                "quantity": 1
            }
        ]

    def test_same_results(self):
        original, _ = original_process(self.data)
        optimized, _ = optimized_process(self.data)

        self.assertEqual(original, optimized)

    def test_total_sales(self):
        result, _ = optimized_process(self.data)

        self.assertEqual(result["total_sales"], 1200)

    def test_average_price(self):
        result, _ = optimized_process(self.data)

        self.assertAlmostEqual(
            result["average_price"],
            200
        )

    def test_empty_data(self):
        result, _ = optimized_process([])

        self.assertEqual(result["total_sales"], 0)
        self.assertEqual(result["average_price"], 0)
        self.assertEqual(result["duplicates"], [])


if __name__ == "__main__":
    unittest.main()
