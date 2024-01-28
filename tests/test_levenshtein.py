from strmetrics.levenshtein import Levenshtein
import unittest


class TestLevenshteinNormalized(unittest.TestCase):
    def test_levenshtein_normalized(self):
        d = Levenshtein()

        self.assertEqual(d.distance("Hi", "Hello"), 4)


if __name__ == '__main__':
    unittest.main()
