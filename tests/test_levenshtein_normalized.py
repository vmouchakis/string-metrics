from strmetrics.levenshtein_normalized import LevenshteinNormalized
import unittest


class TestLevenshteinNormalized(unittest.TestCase):
    def test_levenshtein_normalized(self):
        d = LevenshteinNormalized()

        self.assertEqual(round(d.distance("Hi", "Hello"), 1), 0.2)


if __name__ == '__main__':
    unittest.main()
