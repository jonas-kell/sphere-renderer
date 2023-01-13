import numpy as np
import math

from coordinates import (
    get_2d_coordinates_of_pentagons,
    get_3d_coordinates_of_pentagons,
    get_2d_coordinates,
    get_3d_coordinates,
    get_2d_to_3d,
    get_3d_to_2d,
)


def get_2d_coordinate_from_circle_coordinate(circle_x, circle_y):
    sphere_x, sphere_y, sphere_z = circle_coordinate_to_sphere_coordinate(
        circle_x, circle_y
    )

    if sphere_x > sphere_y:
        return 0, 0
    else:
        return 1, 0


def circle_coordinate_to_sphere_coordinate(circle_x, circle_y):
    return (
        circle_x,
        circle_y,
        math.sqrt(1 - circle_x**2 - circle_y**2 + 0.0001),
    )  # add small value for avoiding math domain errors
