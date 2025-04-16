from __future__ import annotations


class Vector:
    # region vector_init
    def __init__(self, *components: float):
        self.components = tuple(components)

    def __repr__(self) -> str:
        return f"Vector{self.components}"
        # endregion vector_init

    # region vector_equality
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and self.components == other.components
        # endregion vector_equality

    # region vector_dimension
    def __len__(self) -> int:
        return len(self.components)

    def __getitem__(self, i: int) -> float:
        return self.components[i]
        # endregion vector_dimension

    # region vector_addition
    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

        components = (a + b for a, b in zip(self, other))
        return Vector(*components)
        # endregion vector_addition

    # region vector_scalar_multiplication
    def __mul__(self, scalar: float) -> Vector:
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar multiplication only supports int or float.")

        components = (x * scalar for x in self)
        return Vector(*components)

    def __rmul__(self, scalar: float) -> Vector:
        return self * scalar

    def __truediv__(self, scalar: float) -> Vector:
        return (1 / scalar) * self
        # endregion vector_scalar_multiplication

    # region vector_magnitude
    def __abs__(self) -> float:
        return sum(x**2 for x in self) ** 0.5
        # endregion vector_magnitude

    # region vector_unit
    def unit(self) -> Vector:
        magnitude = abs(self)

        if magnitude == 0:
            raise ValueError("Cannot unitise a zero vector")

        return self / magnitude
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
            raise ValueError("Dot product requires a vector")

        if len(self) != len(other):
            raise ValueError("Vectors must have same length")

        return sum(x * y for x, y in zip(self, other))
        # endregion dot_product

    # region vector_cosine
    def cosine(self, other: Vector) -> float:
        return self.unit().dot(other.unit())
        # endregion vector_cosine

    # region vector_cross_product_2d
    def cross(self, other: Vector) -> float:
        if not isinstance(other, Vector):
            return NotImplemented

        if len(self) == len(other) == 2:
            return self[0] * other[1] - other[0] * self[1]
            # endregion vector_cross_product_2d

        if len(self) == len(other) == 3:
            return Vector(
                self[1] * other[2] - self[2] * other[1],
                self[2] * other[0] - self[0] * other[2],
                self[0] * other[1] - self[1] * other[0],
            )

        raise ValueError("Cross product is only defined for 2D or 3D vectors.")
