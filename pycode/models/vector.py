from __future__ import annotations
from typing import Iterable, Sequence, overload
from math import sqrt


# region vector_init
class Vector:
    def __init__(self, components: Iterable[float]):
        self._components = tuple(components)

    @property
    def components(self):
        return self._components

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self.components == other.components
        # endregion vector_init

    def __repr__(self) -> str:
        return f"Vector{self.components}"

    def __hash__(self) -> int:
        return hash(self.components)

    # region vector_items
    def __getitem__(self, key: int) -> float:
        if isinstance(key, slice):
            return Vector(self.components[key])

        return self.components[key]

    def __iter__(self):
        return iter(self.components)
        # endregion vector_items

    # region vector_dimension
    @property
    def dim(self) -> int:
        return len(self.components)
        # endregion vector_dimension

    # region vector_addition
    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented

        if self.dim != other.dim:
            raise ValueError("Dimension mismatch")

        return Vector(x + y for x, y in zip(self, other))
        # endregion vector_addition

    # region vector_hadamard_product
    @overload
    def __mul__(self, other: int | float) -> Vector: ...

    @overload
    def __mul__(self, other: Vector) -> Vector: ...

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # scalar multiplication
            return Vector(x * other for x in self)

        if isinstance(other, Vector):
            # hadamard product
            return Vector(x * y for x, y in zip(self, other))

        return NotImplemented

    __rmul__ = __mul__
    # endregion vector_hadamard_product

    def __truediv__(self, scalar: float) -> Vector:
        return (1 / scalar) * self

        # region dot_product

    def dot(self, other: Vector) -> float:
        if not isinstance(other, Vector):
            return NotImplemented

        if self.dim != other.dim:
            raise ValueError("Dimension mismatch")

        return sum(self * other)  # uses hadamard prod

    __matmul__ = dot
    # endregion dot_product

    # region vector_magnitude
    def __abs__(self) -> float:
        return sqrt(self @ self)
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

    # region vector_cosine
    def cosine(self, other: Vector) -> float:
        return self.unit() @ other.unit()
        # endregion vector_cosine

    # region vector_perp
    def perp(self):
        if self.dim != 2:
            return NotImplemented

        return Vector([self[1], -self[0]])
        # endregion vector_perp

    # region vector_projection
    def proj(self, target: Vector) -> Vector:
        return (self @ target) / (target @ target) * target
        # endregion vector_projection

    # region vector_area
    @classmethod
    def area(cls, u: Vector, v: Vector):
        return sqrt((u @ u) * (v @ v) - (u @ v) ** 2)
        # endregion vector_area

    # region vector_cross_product
    def omit(self, i: int) -> Vector:
        u = Vector(self.components[:i] + self.components[i + 1 :])
        return u

    @classmethod
    def cross(cls, vectors: Sequence[Vector]) -> Vector:
        dim = len(vectors) + 1

        if any(v.dim != dim for v in vectors):
            raise ValueError("Requires n vectors in (n + 1)-dimensions")

        V = [(-1) ** i * cls.vol([v.omit(i) for v in vectors]) for i in range(dim)]
        return Vector(V)
        # endregion vector_cross_product

    @classmethod
    def vol(cls, vectors: list[Vector]) -> float:
        dim = len(vectors)

        if any(v.dim != dim for v in vectors):
            raise ValueError("Require n vectors in n dimensions")

        if dim == 2:
            u, v = vectors
            return u @ v.perp()

        u, *rest = vectors
        return u @ cls.cross(rest)
