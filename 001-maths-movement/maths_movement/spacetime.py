import dataclasses
import sys

def argtype_enforced(arg_type):
    def argtype_enforced_decorator(func):
        def runtime(self, other):
            if not isinstance(other, arg_type):
                raise TypeError(
                    f"This method for {self.__name__} is only supported with"
                    f" a {arg_type.__name__} instance"
                )
            else:
                pass
            return func(self, other)
        return runtime
    return argtype_enforced_decorator


class Direction:
    value: float = float("+Inf")

    def __init__(self, value):
        if value > 0:
            self.value = float("+Inf")
        else:
            if value < 0:
                self.value = float("-Inf")
            else:
                self.value = 0
        return None

    def __add__(self, other):
        result = None
        if other > 0:
            result = float("+Inf")
        else:
            if other < 0:
                result = float("-Inf")
            else:
                result = self.value
        return result

    def __setattr__(self, name, new_value):
        if new_value > 0:
            self.__dict__[name] = float("+Inf")
        else:
            if new_value < 0:
                self.__dict__[name] = float("-Inf")
            else:
                self.__dict__[name] = 0
        return None

    def __iadd__(self, other):
        if other > 0:
            self.value = float("+Inf")
        else:
            if other < 0:
                self.value = float("-Inf")
            else:
                self.value = 0
        return None

    def __eq__(self, other):
        return self.value == other

    def __ge__(self, other):
        return self.value >= other

    def __gt__(self, other):
        return self.value > other

    def __le__(self, other):
        return self.value <= other

    def __lt__(self, other):
        return self.value < other

    def __ne__(self, other):
        return self.value != other

    def __hash__(self):
        return 1 if self.value > 0 else -1

    def __bool__(self):
        return 1 if self.value > 0 else -1



@dataclasses.dataclass
class SpaceTimeDisplacement:
    dx: float = 0.0
    dy: float = 0.0
    dz: float = 0.0
    dt: float = 0.0

    def __eq__(self, other: "SpaceTimeDisplacement"):
        return all(
            (
                self.dx == other.dx,
                self.dy == other.dy,
                self.dz == other.dz,
                self.dt == other.dt,
            )
        )

    def __ge__(self, other):
        return (
            self == other
            or self > other
        )

    def __gt__(self, other):
        return (
            self.dx > other.dx
            or self.dy > other.dy
            or self.dz > other.dz
            or self.dt > other.dt
        )

    def __le__(self, other):
        return self.value <= other

    def __lt__(self, other):
        return (
            self.dx < other.dx
            or self.dy < other.dy
            or self.dz < other.dz
            or self.dt < other.dt
        )

    def __ne__(self, other):
        return not (self == other)

    def __bool__(self):
        return (
            any(
                (
                    self.dx != 0,
                    self.dy != 0,
                    self.dz != 0,
                    self.dt != 0,
                )
            )
            and all(
                (
                    self.dx is not None,
                    self.dy is not None,
                    self.dz is not None,
                    self.dt is not None,
                )
            )
        )

    def is_valid(self):
        return all(
            (
                self.dx is not None,
                self.dy is not None,
                self.dz is not None,
                self.dt is not None,
            )
        )


@dataclasses.dataclass
class SpaceTimePoint:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    t: float = 0.0

    @argtype_enforced(SpaceTimeDisplacement)
    def __add__(self, other: SpaceTimeDisplacement):
        new_pt = SpaceTimePoint(
            x=self.x + other.dx,
            y=self.y + other.dy,
            z=self.z + other.dz,
            t=self.t + other.dt,
        )
        return new_pt

    @argtype_enforced(SpaceTimeDisplacement)
    def __iadd__(self, other: SpaceTimeDisplacement):
        self.x += other.dx
        self.y += other.dy
        self.z += other.dz
        self.t += other.dt
        return None


    @argtype_enforced("SpaceTimePoint")
    def __matmul__(self, other: "SpaceTimePoint"):
        self.x += other.dx
        self.y += other.dy
        self.z += other.dz
        self.t += other.dt
        return None

    def is_valid(self):
        return all(
            (
                self.x is not None,
                self.y is not None,
                self.z is not None,
                self.t is not None,
            )
        )


@dataclasses.dataclass
class SpaceTimeOrientation:
    ox: float = 0.0
    oy: float = 0.0
    oz: float = 0.0
    ot: Direction = Direction(0)
