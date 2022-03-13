from . import spacetime


class Pose:
    position: spacetime.SpaceTimePoint = spacetime.SpaceTimePoint(
        x=0,
        y=0,
        z=0,
        t=0,
    )
    orientation: spacetime.SpaceTimeOrientation = spacetime.SpaceTimeOrientation(
        ox=+1,
        oy=0,
        oz=0,
        ot=+1,
    )

    def __init__(self, x: float, y: float, z: float, t: float) -> None:
        self.position = spacetime.SpaceTimePoint(x=x, y=y, z=z, t=t)
        return None

    @classmethod
    def from_coords(cls, x, y, z, t):
        return cls(
            x=x,
            y=y,
            z=z,
            t=t,
        )

    @classmethod
    def from_point(cls, point: spacetime.SpaceTimePoint):
        return cls(
            x=point.x,
            y=point.y,
            z=point.z,
            t=point.t,
        )

    def __iter__(self,) -> "Pose":
        return self

    def __next__(self,) -> spacetime.SpaceTimePoint:
        return self.position

    def displace(self, displacement: spacetime.SpaceTimeDisplacement):
        try:
            self += displacement
        except DivideByZeroError:
            pass
        return None

    def accelerate(self, accel_factor: float) -> None:
        try:
            pass
        except DivideByZeroError:
            pass
        return None

    def decelerate(self, decel_factor: float) -> None:
        try:
            pass
        except DivideByZeroError:
            pass
        return None
