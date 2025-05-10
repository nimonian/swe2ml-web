from __future__ import annotations
from typing import Iterable

from pycode.models.vector import Vector


def cross(vectors: list[Vector]) -> Vector:
    n = len(vectors) + 1

    if n == 2:
        v = vectors[0]
        return Vector([v[1], -v[0]])

    return Vector((-1) ** i * vol(v.omit(i) for v in vectors) for i in range(n))


def vol(vectors: Iterable[Vector]) -> float:
    vectors = list(vectors)
    u, rest = vectors[0], vectors[1:]
    return u @ cross(rest)
