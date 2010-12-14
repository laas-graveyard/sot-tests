
# Robots.
class Hrp2_10:
    pass

class Hrp2_14:
    pass

class InitialPosition(object):
    """
    This class defines the robot starting position.
    It defines the position of:
    - the left and right lefts
    - the left and right arms
    - the left and right hands
    - the chest
    - the head

    An initial position is required to instantiate an experiment.
    """
    def __init__(self, lleg, rleg, chest, head, larm, rarm, lhand, rhand):
        self.lleg = lleg
        self.rleg = rleg
        self.chest = chest
        self.head = head
        self.larm = larm
        self.rarm = rarm
        self.lhand = lhand
        self.rhand = rhand

defaultInitialPositions = {
    Hrp2_10:
    InitialPosition(
        "0 0 -26 50 -24 0",
        "0 0 -26 50 -24 0",
        "0 0",
        "0 0",
        "15  10 0 -30 0 0 0 10",
        "15 -10 0 -30 0 0 0 10",
        "-10.0 10.0 -10.0 10.0 -10.0",
        "-10.0 10.0 -10.0 10.0 -10.0"),

    Hrp2_14:
    InitialPosition(
        "0 0 -26 50 -24 0",
        "0 0 -26 50 -24 0",
        "0 0",
        "0 0",
        "15  10 0 -30 0 0 10",
        "15 -10 0 -30 0 0 10",
        "-10.0 10.0 -10.0 10.0 -10.0",
        "-10.0 10.0 -10.0 10.0 -10.0")
    }

