from __future__ import annotations
from typing import Iterable
from pycode.models.vector import Vector


# region plane_init
class Plane:
    def __init__(self, origin: Iterable[float], normal: Vector):
        self._origin = Vector(origin)
        self._normal = normal

    @property
    def origin(self) -> Vector:
        return self._origin

    @property
    def normal(self) -> Vector:
        return self._normal
        # endregion plane_init

    def __repr__(self) -> str:
        return f"Plane(origin={self.origin}, normal={self.normal})"

    # region plane_contains
    def __contains__(self, point: Iterable[float]) -> bool:
        return self.normal @ (Vector(point) - self.origin) == 0
        # endregion plane_contains

    # region plane_from_points
    def from_points(points: Iterable[Iterable[float]]) -> Plane:
        if len(points) != 3:
            return NotImplemented

        p0, p1, p2 = [Vector(point) for point in points]
        d1, d2 = p1 - p0, p2 - p0
        return Plane(p0, Vector.cross([d1, d2]))
        # endregion plane_from_points
