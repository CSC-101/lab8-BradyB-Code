import group
import unittest


class TestCases(unittest.TestCase):

    def test_groups_o3_1(self):
        input = [2,3,4,4,5,6,3,5,6,6]
        result = group.groups_of_3(input)
        expected = [[2,3,4],[4,5,6],[3,5,6],[6]]
        self.assertEqual(expected, result)

    def test_groups_o3_2(self):
        input = [2,3,4,4,5,6,3,5,6,6,7,8]
        result = group.groups_of_3(input)
        expected = [[2,3,4],[4,5,6],[3,5,6],[6,7,8]]
        self.assertEqual(expected, result)

    def test_groups_o3_3(self):
        input = [2,3,4,4,5,6,3,5,6,6,7]
        result = group.groups_of_3(input)
        expected = [[2,3,4],[4,5,6],[3,5,6],[6,7]]
        self.assertEqual(expected, result)

