import unittest
import re

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = '^(\s+)?[+-]?(\.?\d+|\d+\.?)(\d+)?(e[+-]?\d+)?(\s+)?$'
        return re.match(pattern, s) != None

class TestSolution(unittest.TestCase):
    def test(self):
        test_cases = [
            ['0', True],
            [' 0.1 ', True],
            ['abc', False],
            ['1 a', False],
            ['2e10', True],
            ['.1', True],
            ['.1.', False],
        ]

        for [s, expected] in test_cases:
            out = Solution().isNumber(s)
            self.assertEqual(out, expected, s)

