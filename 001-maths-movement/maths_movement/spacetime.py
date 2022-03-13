import dataclasses


@dataclasses.dataclass
class SpaceTimeDisplacement:
    dx: float = 0.0
    dy: float = 0.0
    dz: float = 0.0
    dt: float = 0.0


@dataclasses.dataclass
class SpaceTimePoint:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    t: float = 0.0

    def __add__(self, other: SpaceTimeDisplacement):
        new_pt = SpaceTimePoint(
            x=self.x + other.dx,
            y=self.y + other.dy,
            z=self.z + other.dz,
            t=self.t + other.dt,
        )
        return new_pt

    def __addeq__(self, other: SpaceTimeDisplacement):
        self.x += other.dx
        self.y += other.dy
        self.z += other.dz
        self.t += other.dt
        return None
