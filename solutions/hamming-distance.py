"""
https://leetcode.com/problems/hamming-distance/description/

1,2,3     -> 3
1,2,3,4,5 -> 5
"""

import unittest


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x > y:
            x, y = y, x
        bits_x = bin(x)[2:]
        bits_y = bin(y)[2:]
        len_x = len(bits_x)
        len_y = len(bits_y)
        distance = 0

        for iy, by in enumerate(bits_y):
            ix = iy - (len_y - len_x)
            if ix < 0:
                if by == '1':
                    distance += 1
            else:
                bx = bits_x[ix]
                if bx != by:
                    distance += 1
        return distance


class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            Solution().hammingDistance(0, 0),
            0,
        )
        self.assertEqual(
            Solution().hammingDistance(1, 4),
            2,
        )


if __name__ == 'main':
    unittest.main()
