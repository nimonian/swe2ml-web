from __future__ import annotations
from typing import Iterable, overload
from math import sqrt


class Vector:
    # region vector_init
    def __init__(self, components: Iterable[float]):
        self._components = tuple(components)

    @property
    def components(self):
        return self._components
        # endregion vector_init

    def __repr__(self) -> str:
        return f"Vector{self.components}"

    def __hash__(self) -> int:
        return hash(self.components)

    # region vector_equality
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self.components == other.components
        # endregion vector_equality

    # region vector_items
    def __getitem__(self, i: int) -> float:
        return self.components[i]

    def __iter__(self):
        return iter(self.components)
        # endregion vector_items

    # region vector_dimension
    def dim(self) -> int:
        return len(self.components)
        # endregion vector_dimension

    # region vector_addition
    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented

        if self.dim() != other.dim():
            raise ValueError("Dimension mismatch")

        return Vector(a + b for a, b in zip(self, other))
        # endregion vector_addition

    # region vector_scalar_multiplication
    def __mul__(self, scalar: float) -> Vector:
        if not isinstance(scalar, (int, float)):
            return NotImplemented

        return Vector(x * scalar for x in self)

    __rmul__ = __mul__

    def __truediv__(self, scalar: float) -> Vector:
        return (1 / scalar) * self
        # endregion vector_scalar_multiplication

    # region vector_magnitude
    def __abs__(self) -> float:
        return sqrt(sum(x**2 for x in self))
        # endregion vector_magnitude

    # region vector_unit
    def unit(self) -> Vector:
        return self / abs(self)
        # endregion vector_unit

    # region vector_subtraction
    def __neg__(self) -> Vector:
        return -1 * self

    def __sub__(self, other: Vector) -> Vector:
        return self + (-other)
        # endregion vector_subtraction

    # region dot_product
    def dot(self, other: Vector) -> float:
        if not isinstance(other, Vector):
            return NotImplemented

        if self.dim() != other.dim():
            raise ValueError("Dimension mismatch")

        return sum(x * y for x, y in zip(self, other))

    __matmul__ = dot
    # endregion dot_product

    # region vector_cosine
    def cosine(self, other: Vector) -> float:
        return self.unit() @ other.unit()
        # endregion vector_cosine

    # region vector_cross_product_2d
    def cross(self, other: Vector) -> float | Vector:
        if not isinstance(other, Vector):
            return NotImplemented

        if self.dim() == other.dim() == 2:
            return self[0] * other[1] - other[0] * self[1]
            # endregion vector_cross_product_2d

        if self.dim() == other.dim() == 3:
            return Vector(
                [
                    self[1] * other[2] - self[2] * other[1],
                    self[2] * other[0] - self[0] * other[2],
                    self[0] * other[1] - self[1] * other[0],
                ]
            )

        raise ValueError("Cross product is only defined for 2D or 3D vectors.")

    __xor__ = cross
