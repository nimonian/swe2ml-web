from pycode.models.plane import Plane
from pycode.models.vector import Vector


# region plane_init
def test_plane_init():
    p = Vector([2, 0, -1])
    n = Vector([4, 1, 3])
    plane = Plane(p, n)

    assert plane.origin == p
    assert plane.normal == n
    # endregion plane_init


# region plane_contains
def test_plane_contains():
    p = Vector([2, 0, -1])
    n = Vector([4, 1, 3])
    plane = Plane(p, n)

    q1 = Vector([0, 2, 1])
    q2 = Vector([1, 1, 1])

    assert q1 in plane
    assert q2 not in plane
    # endregion plane_contains


# region test_plane_from_points
def test_plane_from_points():
    P0, P1, P2 = [1, 0, 2], [-2, 1, 4], [4, -1, 3]
    plane = Plane.from_points([P0, P1, P2])

    # assert plane.normal == Vector([2, 9, 3])
    assert P0 in plane
    assert P1 in plane
    assert P2 in plane
    # endregion test_plane_from_points
