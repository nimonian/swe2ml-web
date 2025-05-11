from pytest import approx
from pycode.models.vector import Vector
from math import sqrt


# region test_vector_components
def test_vector_components():
    v = Vector([1, 2, 3, 4])
    assert v.components == (1, 2, 3, 4)


def test_vector_equality():
    assert Vector([1, 2, 3]) == Vector([1, 2, 3])
    assert Vector([1, 2, 3]) != Vector([1, 2, 4])
    # endregion test_vector_components


def test_vector_repr():
    assert repr(Vector([1, 2, 3])) == "Vector(1, 2, 3)"


# region test_vector_items
def test_vector_getitem():
    v = Vector([1, 2, 3])
    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3


def test_vector_slice():
    v = Vector([1, 2, 3, 4])
    assert v[1:3] == Vector([2, 3])


def test_vector_iter():
    v = Vector([1, 2, 3])
    assert list(v) == [1, 2, 3]
    # endregion test_vector_items


# region test_vector_dimension
def test_vector_dimension():
    u = Vector([1, 2, 3])
    v = Vector([4, 5])
    assert u.dim == 3
    assert v.dim == 2
    # endregion test_vector_dimension


# region test_vector_addition
def test_vector_addition():
    u = Vector([1, 2])
    v = Vector([3, 4])
    assert u + v == Vector([4, 6])
    assert u + v == v + u
    # endregion test_vector_addition


# region test_vector_scalar_multiplication
def test_vector_scalar_multiplication():
    v = Vector([2, 3])
    assert v * 2 == Vector([4, 6])
    assert 2 * v == v * 2
    assert v + v == 2 * v


def test_vector_scalar_division():
    v = Vector([1, 2, -4, 0])
    assert v / 2 == Vector([0.5, 1, -2, 0])
    # endregion test_vector_scalar_multiplication


# region test_vector_subtraction
def test_vector_negative():
    u = Vector([5, -7, 0])
    assert -u == Vector([-5, 7, 0])


def test_vector_subtraction():
    u = Vector([4, -1])
    v = Vector([2, 3])
    assert v - u == Vector([-2, 4])
    # endregion test_vector_subtraction


# region test_vector_magnitude
def test_vector_magnitude():
    v = Vector([3, 4])
    assert abs(v) == 5
    assert abs(2 * v) == 10
    # endregion test_vector_magnitude


# region test_vector_unit
def test_vector_unit():
    v = Vector([3, 4])
    assert v.unit() == Vector([approx(0.6), approx(0.8)])
    assert abs(v.unit()) == 1
    assert (2 * v).unit() == v.unit()
    # endregion test_vector_unit


# region test_hadamard_product
def test_vector_hadamard_product():
    u = Vector([3, 2])
    v = Vector([2, 4])
    assert u * v == Vector([6, 8])
    # endregion test_hadamard_product


# region test_dot_product
def test_dot_product():
    u = Vector([1, 3])
    v = Vector([4, 2])
    assert u @ v == v @ u == 10
    # endregion test_dot_product


# region test_dot_product_2
def test_dot_product_properties():
    u = Vector([1, 3])
    v = Vector([4, 2])

    assert (2 * u) @ (3 * v) == 60
    assert u @ u == approx(abs(u) ** 2)
    assert u @ Vector([-3, 1]) == 0
    # endregion test_dot_product_2


# region test_vector_cosine
def test_vector_cosine():
    a = Vector([2, 3])
    b = Vector([4, 6])
    c = Vector([-3, 2])
    d = Vector([1, -3])

    assert a.cosine(b) == approx(1)
    assert b.cosine(c) == approx(0)
    assert c.cosine(d) == approx(-0.789352)
    # endregion test_vector_cosine


# region test_vector_perp
def test_vector_perp():
    u = Vector([1, 3])
    v = u.perp()
    assert u @ v == 0
    # endregion test_vector_perp


# region test_vector_projection
def test_vector_projection():
    u = Vector([4, 2])
    v = Vector([1, 3])
    assert v.proj(u) == Vector([2, 1])
    # endregion test_vector_projection


# region test_vector_cross_product
def test_vector_cross_product_3d():
    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    n = Vector.cross([u, v])

    assert n == Vector([-3, 6, -3])
    assert u @ n == 0
    assert v @ n == 0
    # endregion test_vector_cross_product


# region test_vector_area
def test_vector_area():
    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])

    area = Vector.area(u, v)

    assert area == approx(sqrt(54))
    assert area == approx(abs(Vector.cross([u, v])))
    # endregion test_vector_area


# region test_linear_combination
def test_linear_combination():
    a = Vector([2, 1])
    b = Vector([1, 3])

    assert 2 * a + b == Vector([5, 5])
    # endregion test_linear_combination


# region test_vector_omit
def test_vector_omit():
    u = Vector([1, 2, 3])
    v = u.omit(1)
    assert v == Vector([1, 3])
    # endregion test_vector_omit


# region test_vol_1d
def test_vector_vol_2d():
    u = Vector([3])
    assert Vector.vol([u]) == 3
    # endregion test_vol_1d


# region test_vol_2d
def test_vector_vol_2d():
    u = Vector([4, 2])
    v = Vector([1, 3])

    assert Vector.vol([u, v]) == 10
    # endregion test_vol_2d


# region test_vol_3d
def test_volume_3d():
    u = Vector([4, -1, 0])
    v = Vector([-2, 1, -3])
    w = Vector([3, 2, 3])

    assert Vector.vol([u, v, w]) == 39
    # endregion test_vol_3d


# region test_vol_4d
def test_volume_4d():
    u = Vector([1, 2, 3, 4])
    v1 = Vector([2, 3, 4, 1])
    v2 = Vector([3, 4, 1, 2])
    v3 = Vector([4, 1, 2, 3])

    assert Vector.vol([u, v1, v2, v3]) == 160
    # endregion test_vol_4d
