import dataclasses


@dataclasses.dataclass
class BoneJoints:
    a:str = None
    b:str = None


class Bone:
    length: float = None
    joints: BoneJoints = BoneJoints(a=None, b=None)

    def __init__(self, length, joint_names):
        self.length = length
        self.joints = BoneJoints(*joint_names)
        return None

    def attach(self, bone, joint):
        return None


class Skeleton:
    def __init__(self, bones):
        self.bones = bones
        return None

    def attach_bone(self, bone, joint_name):
        return None


class HumanSkeleton(Skeleton):
    pass


class GorillaSkeleton(Skeleton):
    pass
