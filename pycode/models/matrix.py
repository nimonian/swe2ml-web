from __future__ import annotations
from typing import Iterable, overload

from pycode.models.vector import Vector


class Matrix:
    # region matrix_init
    def __init__(self, entries: Iterable[Iterable[float]]):
        rows = tuple(tuple(row) for row in entries)

        if any(len(row) != len(rows[0]) for row in rows):
            raise ValueError("All rows must have same length")

        self._rows = rows

    @property
    def rows(self):
        return self._rows

    @property
    def cols(self):
        return tuple(zip(*self.rows))
        # endregion matrix_init

    def __eq__(self, other: Matrix) -> bool:
        return isinstance(other, Matrix) and self.rows == other.rows

    # region matrix_shape
    @property
    def shape(self) -> tuple[int, int]:
        return len(self.rows), len(self.cols)
        # endregion matrix_shape

    # region matrix_entry
    def __getitem__(self, key) -> float:
        i, j = key
        return self.rows[i][j]

    def __iter__(self):
        return iter(self.rows)
        # endregion matrix_entry

    # region matrix_transpose
    def transpose(self) -> Matrix:
        return Matrix(self.cols)
        # endregion matrix_transpose

    # region matrix_addition
    def __add__(self, other: Matrix) -> Matrix:
        if self.shape != other.shape:
            raise ValueError("Dimension mismatch")

        A = [Vector(row) for row in self]
        B = [Vector(row) for row in other]
        return Matrix(u + v for u, v in zip(A, B))
        # endregion matrix_addition

    # region matrix_matrix_multiplication
    @overload
    def __matmul__(self, other: Matrix) -> Matrix: ...

    # region matrix_vector_multiplication
    @overload
    def __matmul__(self, other: Vector) -> Vector: ...

    def __matmul__(self, other):
        if isinstance(other, Vector):
            components = [Vector(row) @ other for row in self]
            return Vector(components)
            # endregion matrix_vector_multiplication

        if isinstance(other, Matrix):
            rows = [Vector(row) for row in self.rows]
            cols = [Vector(col) for col in other.cols]
            return Matrix([row @ col for col in cols] for row in rows)
            # endregion matrix_matrix_multiplication

    # region matrix_scalar_multiplication
    def __mul__(self, other: float) -> Matrix:
        if isinstance(other, (int, float)):
            return Matrix([other * x for x in row] for row in self)

        return NotImplemented

    __rmul__ = __mul__
    # endregion matrix_scalar_multiplication

    # region matrix_subtraction
    def __neg__(self) -> Matrix:
        return -1 * self

    def __sub__(self, other: Matrix) -> Matrix:
        return self + (-other)
        # endregion matrix_subtraction

    # region identity_matrix
    @classmethod
    def I(cls, n: int) -> Matrix:
        return cls([int(i == j) for i in range(n)] for j in range(n))
        # endregion identity_matrix

    # region matrix_det_2d
    def det(self) -> float:
        m, n = self.shape

        if m != n:
            raise ValueError("Matrix must be square")

        if m == n == 2:
            u, v = [Vector(col) for col in self.cols]
            return u.cross(v)
            # endregion matrix_det_2d
