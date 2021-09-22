"""
Tests for the basic vector math class
"""

import unittest
from space import main

class VectorMathTestCase(unittest.TestCase):
    """
    Test case for the basic vector math class
    """
    def test_distance_between_pts(self):
        """
        Test for distance between points
        """
        point_1 = main.Point(0, 0, 0)
        point_2 = main.Point(3, 4, 0)
        distance = main.VectorMath.calc_distance_between_pts(point_1, point_2)
        self.assertEqual(5.0, distance)
