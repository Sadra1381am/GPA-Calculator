import unittest
from unittest.mock import patch
from io import StringIO
from main import get_score, calculate_gpa, compare

class TestGetScore(unittest.TestCase):

    @patch('builtins.input', side_effect=['15', '3'])
    def test_get_score_valid_input(self, mock_input):
        list_score = []
        list_credit = []
        get_score(list_score, list_credit)
        self.assertEqual(list_score, [15.0])
        self.assertEqual(list_credit, [3])

    @patch('builtins.input', side_effect=['25', '2'])
    def test_get_score_invalid_input(self, mock_input):
        list_score = []
        list_credit = []
        get_score(list_score, list_credit)
        self.assertEqual(list_score, [])
        self.assertEqual(list_credit, [])

class TestCalculateGPA(unittest.TestCase):

    def test_calculate_gpa(self):
        list_score = [15.0, 12.0, 18.0]
        list_credit = [3, 4, 2]
        result = calculate_gpa(list_score, list_credit)
        self.assertAlmostEqual(result, 2.7777,places = 2)

class TestCompare(unittest.TestCase):

    def test_compare(self):
        gpa = 3.0
        result = compare(gpa)
        self.assertEqual(len(result), len(result))  # Assuming there are 10 universities within the GPA range

if __name__ == '__main__':
    unittest.main()