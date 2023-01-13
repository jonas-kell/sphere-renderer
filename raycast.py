# https://www.erikrotteveel.com/python/three-dimensional-ray-tracing-in-python/

import numpy as np

# source: http://geomalgorithms.com/a06-_intersect-2.html
def ray_intersect_triangle(p0, p1, triangle):
    # Tests if a ray starting at point p0, in the direction
    # p1 - p0, will intersect with the triangle.
    #
    # arguments:
    # p0, p1: numpy.ndarray, both with shape (3,) for x, y, z.
    # triangle: numpy.ndarray, shaped (3,3), with each row
    #     representing a vertex and three columns for x, y, z.
    #
    # returns:
    #    0.0 if ray does not intersect triangle,
    #    1.0 if it will intersect the triangle,
    #    2.0 if starting point lies in the triangle.
    v0, v1, v2 = triangle
    u = v1 - v0
    v = v2 - v0
    normal = np.cross(u, v)
    b = np.inner(normal, p1 - p0)
    a = np.inner(normal, v0 - p0)

    # Here is the main difference with the code in the link.
    # Instead of returning if the ray is in the plane of the
    # triangle, we set rI, the parameter at which the ray
    # intersects the plane of the triangle, to zero so that
    # we can later check if the starting point of the ray
    # lies on the triangle. This is important for checking
    # if a point is inside a polygon or not.

    if b == 0.0:
        # ray is parallel to the plane
        if a != 0.0:
            # ray is outside but parallel to the plane
            return 0
        else:
            # ray is parallel and lies in the plane
            rI = 0.0
    else:
        rI = a / b
    if rI < 0.0:
        return 0
    w = p0 + rI * (p1 - p0) - v0
    denom = np.inner(u, v) * np.inner(u, v) - np.inner(u, u) * np.inner(v, v)
    si = (np.inner(u, v) * np.inner(w, v) - np.inner(v, v) * np.inner(w, u)) / denom

    if (si < 0.0) | (si > 1.0):
        return 0
    ti = (np.inner(u, v) * np.inner(w, u) - np.inner(u, u) * np.inner(w, v)) / denom

    if (ti < 0.0) | (si + ti > 1.0):
        return 0
    if rI == 0.0:
        # point 0 lies ON the triangle. If checking for
        # point inside polygon, return 2 so that the loop
        # over triangles can stop, because it is on the
        # polygon, thus inside.
        return 2
    return 1


# https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle/barycentric-coordinates.html
# https://courses.cs.washington.edu/courses/csep557/10au/lectures/triangle_intersection.pdf
def get_barycentric_coordinates(p0, p1, triangle):
    # Assuming, the ray cast from p0 to p1 hits the triangle defined by triangle,
    # this returns the barycentric coordinates (https://en.wikipedia.org/wiki/Barycentric_coordinate_system)
    # to the intersection point
    #
    # arguments:
    # p0, p1: numpy.ndarray, both with shape (3,) for x, y, z.
    # triangle: numpy.ndarray, shaped (3,3), with each row
    #     representing a vertex and three columns for x, y, z.
    #
    # returns:
    #    u, v, w the barycentric coordinates, where u * A + v * B + w * C = P, the intersection point

    a, b, c = triangle
    ba = b - a
    ca = c - a
    normal = np.cross(ba, ca)

    d = np.inner(normal, a)

    t = (d - np.inner(normal, p0)) / np.inner(normal, p1 - p0)

    Q = p0 + t * (p1 - p0)
    # print(Q)  # Works

    whole_triangle_area = triangle_area(a, b, c)
    # print(whole_triangle_area)  # Works
    v = triangle_area(c, a, Q) / whole_triangle_area
    w = triangle_area(a, b, Q) / whole_triangle_area

    u = 1 - v - w

    # print(u * a + v * b + w * c)  # Works

    return u, v, w


def triangle_area(p1, p2, p3):
    return 0.5 * np.linalg.norm(np.cross(p2 - p1, p3 - p1))


if __name__ == "__main__":

    print(
        get_barycentric_coordinates(
            np.array([0, 0, 0]),
            np.array([2.3, 2.52, 1.59]),
            np.array([[0, 0, 1], [0, 2, 0], [3, 0, 0]]),
        )
    )
    # Q = (0.64, 0.7, 0.44)
