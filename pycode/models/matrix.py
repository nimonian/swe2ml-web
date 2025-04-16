from __future__ import annotations
from typing import overload
from pycode.models.vector import Vector


class Matrix:
    # region matrix_init
    def __init__(self, rows):
        if any(len(row) != len(rows[0]) for row in rows):
            raise ValueError("All rows must have same length")

        self.rows = tuple(tuple(row) for row in rows)
        # endregion matrix_init

    def __repr__(self) -> str:
        return "Matrix(\n" + "\t\n".join(str(row) for row in self.rows) + "\n)"

    # region matrix_shape
    def shape(self) -> tuple[int, int]:
        return len(self.rows), len(self.rows[0])
        # endregion matrix_shape

    # region matrix_entry
    def __getitem__(self, key) -> float:
        i, j = key
        return self.rows[i][j]

    def row(self, i) -> tuple[float]:
        _, n = self.shape()
        return tuple(self[i, j] for j in range(n))

    def col(self, j) -> tuple[float]:
        m, _ = self.shape()
        return tuple(self[i, j] for i in range(m))
        # endregion matrix_entry

    def __iter__(self):
        return iter(self.rows)

    def __eq__(self, other: Matrix) -> bool:
        if not isinstance(other, Matrix):
            return False

        if self.shape() != other.shape():
            return False

        return all(a == b for a, b in zip(self, other))

    # region matrix_transpose
    def transpose(self) -> Matrix:
        _, n = self.shape()
        cols = [self.col(j) for j in range(n)]
        return Matrix(cols)
        # endregion matrix_transpose

    # region matrix_addition
    def __add__(self, other: Matrix) -> Matrix:
        return Matrix([[x + y for x, y in zip(a, b)] for a, b in zip(self, other)])
        # endregion matrix_addition

    # region matrix_matrix_multiplication
    @overload
    def __mul__(self, other: Matrix) -> Matrix: ...

    # region matrix_scalar_multiplication
    @overload
    def __mul__(self, other: float) -> Matrix: ...

    # region matrix_vector_multiplication
    @overload
    def __mul__(self, other: Vector) -> Vector: ...

    def __mul__(self, other):

        if isinstance(other, Vector):
            _, n = self.shape()
            if n != len(other):
                raise ValueError("Matrix width must equal vector dimension")

            components = (Vector(*row) @ other for row in self)
            return Vector(*components)
            # endregion matrix_vector_multiplication

        if isinstance(other, (int, float)):
            return Matrix([[other * x for x in row] for row in self])
            # endregion matrix_scalar_multiplication

        if isinstance(other, Matrix):
            _, n = self.shape()
            p, _ = other.shape()

            if n != p:
                raise ValueError("Matrices wrong shape for multiplication")

            rows = [Vector(*row) for row in self]
            cols = [Vector(*row) for row in other.transpose()]
            return Matrix([[r @ c for c in cols] for r in rows])
            # endregion matrix_matrix_multiplication

        return NotImplemented

    def __rmul__(self, scalar: float):
        if isinstance(scalar, (int, float)):
            return self * scalar

        return NotImplemented

    # region matrix_subtraction
    def __neg__(self) -> Matrix:
        return -1 * self

    def __sub__(self, other: Matrix) -> Matrix:
        return self + (-other)
        # endregion matrix_subtraction

    # region identity_matrix
    @classmethod
    def I(cls, n: int) -> Matrix:
        return cls([[int(i == j) for i in range(n)] for j in range(n)])
        # endregion identity_matrix

    # region matrix_det_2d
    def det(self) -> float:
        m, n = self.shape()

        if m == n == 2:
            a, b = self.row(0)
            c, d = self.row(1)
            return a * d - b * c
            # endregion matrix_det_2d
