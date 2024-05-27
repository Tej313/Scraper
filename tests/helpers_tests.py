import unittest
from Scraper.helpers import example_helper

class TestHelpers(unittest.TestCase):
    def test_example_helper(self):
        result = example_helper("test")
        self.assertEqual(result, "expected result")

if __name__ == '__main__':
    unittest.main()
