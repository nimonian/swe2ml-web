from __future__ import annotations
from typing import Sequence

from pycode.models.vector import Vector


def vol(vectors: Sequence[Vector]):
    n = len(vectors)

    if n == 2:
        u, v = vectors
        p = Vector([v[1], -v[0]])
        return u @ p

    u, rest = vectors[0], vectors[1:]

    p = Vector([(-1) ** i * vol(rest[:i] + rest[i + 1 :]) for i in range(n - 1)])

    return u @ p
