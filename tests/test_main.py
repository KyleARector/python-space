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
        Test for distance between two points
        """
        point_1 = main.Point(0, 0, 0)
        point_2 = main.Point(3, 4, 0)
        distance = main.VectorMath.calc_distance_between_pts(point_1, point_2)
        self.assertEqual(5.0, distance)

    def test_distance_between_pts_in_list(self):
        """
        Test for getting the closest point to origin from a list
        """
        points = [
            main.Point(3, 4, 0),
            main.Point(0.1, 0.2, 0.3),
            main.Point(0, 5, 4),
            main.Point(-1, 2, -0.3),
            main.Point(100, 0.2, 0.3)
        ]
        actual_closest = main.Point(0.1, 0.2, 0.3)
        calc_closest = main.VectorMath.get_closest_point_from_list(points)
        self.assertEqual(actual_closest, calc_closest)
