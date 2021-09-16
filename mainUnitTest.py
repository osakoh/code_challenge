import unittest
from main import GroupArrayElements


class TestMainUnit(unittest.TestCase):
    def test_group_array_elements(self):
        test = GroupArrayElements([1, 2, 4, 5], 3)
        actual = test.result
        expected = [[1, 2], [4, 5], []]
        self.assertEqual(actual, expected)
