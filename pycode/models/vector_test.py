from pytest import approx
from pycode.models.vector import Vector


# region test_vector_components
def test_vector_components():
    v = Vector([1, 2, 3, 4])
    assert v.components == (1, 2, 3, 4)


def test_vector_repr():
    assert repr(Vector([1, 2, 3])) == "Vector(1, 2, 3)"
    # endregion test_vector_components


# region test_vector_subtraction
def test_vector_subtraction():
    u = Vector([4, -1])
    v = Vector([2, 3])

    assert v - u == Vector([-2, 4])
    # endregion test_vector_subtraction


# region test_vector_equality
def test_vector_equality():
    assert Vector([1, 2, 3]) == Vector([1, 2, 3])
    assert Vector([1, 2, 3]) != Vector([1, 2, 4])
    # endregion test_vector_equality


# region test_vector_dimension
def test_vector_dimension():
    u = Vector([1, 2, 3])
    v = Vector([4, 5])

    assert u.dim() == 3
    assert v.dim() == 2
    # endregion test_vector_dimension


# region test_vector_items
def test_vector_getitem():
    v = Vector([1, 2, 3])

    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3


def test_vector_iter():
    v = Vector([1, 2, 3])
    assert list(v) == [1, 2, 3]
    # endregion test_vector_items


# region test_vector_addition
def test_vector_addition():
    v1 = Vector([1, 2])
    v2 = Vector([3, 4])

    assert v1 + v2 == Vector([4, 6])
    assert v2 + v1 == Vector([4, 6])
    # endregion test_vector_addition


# region test_vector_scalar_multiplication
def test_vector_scalar_multiplication():
    v = Vector([2, 3])

    assert v * 2 == Vector([4, 6])
    assert 2 * v == Vector([4, 6])
    assert v + v == 2 * v
    # endregion test_vector_scalar_multiplication


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
    assert (2 * v).unit() == v.unit()
    # endregion test_vector_unit


# region test_dot_product
def test_dot_product():
    u = Vector([1, 3])
    v = Vector([4, 2])

    assert u @ v == v @ u == 10
    assert (2 * u) @ (3 * v) == 60
    # endregion test_dot_product


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


# region test_vector_cross_product_2d
def test_vector_cross_product_2d():
    u = Vector([3, 1])
    v = Vector([2, 3])

    assert u ^ v == 7
    assert v ^ u == -7
    # endregion test_vector_cross_product_2d


# region test_vector_cross_product_3d
def test_vector_cross_product_3d():
    u = Vector([1, 2, 3])
    v = Vector([4, 5, 6])
    n = u ^ v

    assert n == Vector([-3, 6, -3])
    assert u @ n == 0
    assert v @ n == 0
    # endregion test_vector_cross_product_3d


# region test_linear_combination
def test_linear_combination():
    a = Vector([2, 1])
    b = Vector([1, 3])

    assert 2 * a + b == Vector([5, 5])
    # endregion test_linear_combination
