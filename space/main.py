"""
Basic classes for messing around with vector math in Python
"""

import math
from dataclasses import dataclass

@dataclass
class Point:
    """
    Represents a 3 dimensional point
    """
    x_pos: float
    y_pos: float
    z_pos: float

class VectorMath:
    """
    Class to hold some static vector math functions
    """
    @staticmethod
    def calc_distance_between_pts(point_1, point_2):
        """
        Returns the absolute distance between two 3 dimensional points
        """
        return math.sqrt(
            (point_1.x_pos - point_2.x_pos) ** 2 +
            (point_1.y_pos - point_2.y_pos) ** 2 +
            (point_1.z_pos - point_2.z_pos) ** 2)

    @staticmethod
    def get_point_closest_to_origin(point_1, point_2):
        """
        Returns the point that is closest to 0,0,0
        """
        origin = Point(0, 0, 0)
        point_1_dist_to_origin = VectorMath.calc_distance_between_pts(origin, point_1)
        point_2_dist_to_origin = VectorMath.calc_distance_between_pts(origin, point_2)
        point_1_closer = point_1_dist_to_origin < point_2_dist_to_origin
        return point_1 if point_1_closer else point_2
