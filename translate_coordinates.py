import numpy as np
import math
from raycast import ray_intersect_triangle

from coordinates import (
    get_2d_coordinates_of_pentagons,
    get_2d_coordinates,
    get_3d_coordinates,
    get_2d_to_3d,
    get_3d_to_2d,
)


def get_2d_coordinate_from_circle_coordinate(circle_x, circle_y):
    sphere_x, sphere_y, sphere_z = circle_coordinate_to_sphere_coordinate(
        circle_x, circle_y
    )

    return find_intersected_triangle_in_2d_and_transform_coordinates(
        sphere_x, sphere_y, sphere_z
    )


def circle_coordinate_to_sphere_coordinate(circle_x, circle_y):
    return (
        circle_x,
        circle_y,
        math.sqrt(1 - circle_x**2 - circle_y**2 + 0.0001),
    )  # add small value for avoiding math domain errors


def find_intersected_triangle_in_2d_and_transform_coordinates(
    sphere_x, sphere_y, sphere_z
):
    get_triangle_cache()

    if sphere_x > sphere_y:
        return 0, 0
    else:
        return 1, 0


triangle_cache = None

# all points are python ndarrays
# -> ([3d_triangle_point_1, 3d_triangle_point_2, 3d_triangle_point_3], [2d_triangle_point_1, 2d_triangle_point_2, 2d_triangle_point_3])
def get_triangle_cache():
    global triangle_cache
    if triangle_cache is None:
        triangle_cache = []

        for pentagon in get_2d_coordinates_of_pentagons():
            points_2d = []
            points_3d = []
            for point_2d in pentagon:
                points_2d.append(np.array(point_2d))
                points_3d.append(np.array(get_3d_to_2d(point_2d)))

            center_2d = np.average(points_2d, axis=0)
            center_3d = np.average(points_3d, axis=0)

            for i in range(0, 5):
                triangle_cache.append(
                    (
                        np.array([center_2d, points_2d[i], points_2d[(i + 1) % 5]]),
                        np.array([center_3d, points_3d[i], points_3d[(i + 1) % 5]]),
                    )
                )

    return triangle_cache
