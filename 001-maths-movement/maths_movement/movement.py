from . import spacetime


class Movement:
    position = spacetime.SpaceTimePoint(x=0, y=0, z=0, t=0)

    def __init__(self, x, y, z, t):
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

    def __iter__(self,):
        return self

    def __next__(self,):
        return self.position

    def displace(self, displacement: spacetime.SpaceTimeDisplacement):
        self += displacement
        return None

    def accelerate(self, accel_factor):
        pass

    def decelerate(self, decel_factor):
        pass

