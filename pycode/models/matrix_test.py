import pytest
from pycode.models.matrix import Matrix
from pycode.models.vector import Vector


# region test_matrix_init
def test_matrix_init():
    A = Matrix([[2, -5], [0, 3], [7, 1]])
    assert A.rows == ((2, -5), (0, 3), (7, 1))


def test_matrix_must_be_rectangular():
    with pytest.raises(ValueError):
        Matrix([[1, 2], [3]])
    # endregion test_matrix_init


# region test_matrix_shape
def test_matrix_shape():
    A = Matrix([[2, -5], [0, 3], [7, 1]])
    B = Matrix([[1, 0, -2], [5, -3, 4]])

    assert A.shape() == (3, 2)
    assert B.shape() == (2, 3)
    # endregion test_matrix_shape


# region test_matrix_entry
def test_matrix_entry():
    A = Matrix([[2, -5], [0, 3], [7, 1]])
    B = Matrix([[1, 0, -2], [5, -3, 4]])

    assert A[0, 1] == -5
    assert B[1, 2] == 4


def test_matrix_row():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    assert A.row(0) == (1, 2, 3)
    assert A.row(1) == (4, 5, 6)


def test_matrix_col():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    assert A.col(0) == (1, 4)
    assert A.col(1) == (2, 5)
    assert A.col(2) == (3, 6)
    # endregion test_matrix_entry


# region test_matrix_equality
def test_matrix_equality():
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[1, 2], [3, 4]])
    C = Matrix([[1, 2], [3, 5]])

    assert A == B
    assert A != C
    # endregion test_matrix_equality


# region test_matrix_transpose
def test_matrix_transpose():
    A = Matrix([[1, 2, 3], [4, 5, 6]])
    B = A.transpose()

    assert B == Matrix([[1, 4], [2, 5], [3, 6]])
    assert B.transpose() == A
    # endregion test_matrix_transpose


# region test_matrix_addition
def test_matrix_addition():
    A = Matrix([[3, -1], [4, 2]])
    B = Matrix([[5, 0], [-2, 7]])

    assert A + B == Matrix([[8, -1], [2, 9]])
    assert B + A == Matrix([[8, -1], [2, 9]])


def test_right_distributivity():
    A = Matrix([[1, 0], [0, 2]])
    B = Matrix([[2, 3], [4, 5]])
    v = Vector(1, 2)

    assert (A + B) * v == A * v + B * v
    # endregion test_matrix_addition


# region test_matrix_subtraction
def test_matrix_negative():
    A = Matrix([[1, 2.5], [-3, 0]])
    assert -A == Matrix([[-1, -2.5], [3, 0]])


def test_matrix_subtraction():
    A = Matrix([[3, -1], [4, 2]])
    B = Matrix([[5, 0], [-2, 7]])

    assert A - A == Matrix([[0, 0], [0, 0]])
    assert A - B == Matrix([[-2, -1], [6, -5]])
    # endregion test_matrix_subtraction


# region test_matrix_vector_multiplication
def test_matrix_vector_multiplication():
    A = Matrix([[1, 2], [3, 4]])
    v = Vector(5, 6)

    assert A * v == Vector(17, 39)


def test_left_distributivity():
    A = Matrix([[1, 2], [3, 4]])
    u = Vector(5, 6)
    v = Vector(7, 8)

    assert A * (u + v) == A * u + A * v
    # endregion test_matrix_vector_multiplication


# region test_matrix_scalar_multiplication
def test_matrix_scalar_multiplication():
    A = Matrix([[1, 2], [3, 4]])

    assert 2 * A == Matrix([[2, 4], [6, 8]])
    assert A * 2 == Matrix([[2, 4], [6, 8]])
    assert A + A == 2 * A
    # endregion test_matrix_scalar_multiplication


# region test_matrix_matrix_multiplication
def test_matrix_matrix_multiplication():
    A = Matrix([[2, -1, 4], [0, 3, 5]])
    B = Matrix([[1, 2], [-2, 0], [3, -1]])

    assert A * B == Matrix([[16, 0], [9, -5]])
    assert B * A == Matrix([[2, 5, 14], [-4, 2, -8], [6, -6, 7]])
    # endregion test_matrix_matrix_multiplication


# region test_matrix_composition
def test_matrix_composition():
    A = Matrix([[1, 3], [2, -1]])
    B = Matrix([[-2, 4], [0, 1]])
    v = Vector(3, 2)

    assert (A * B) * v == A * (B * v)
    # endregion test_matrix_composition


# region test_identity_matrix
def test_identity_matrix():
    assert Matrix.I(2) == Matrix([[1, 0], [0, 1]])
    assert Matrix.I(3) == Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


def test_identity_tranformation():
    I = Matrix.I(3)
    v = Vector(1, 2, 3)

    assert I * v == v
    # endregion test_identity_matrix


# region test_matrix_det_2d
def test_matrix_det_2d():
    A = Matrix.I(2)
    B = Matrix([[3, 2], [-1, 4]])

    assert A.det() == 1
    assert B.det() == 14
    # endregion test_matrix_det_2d
