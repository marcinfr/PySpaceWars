from spaceObjects.spaceships.meteor import Meteor
from spaceObjects.spaceships.ship01 import Ship01

class SpaceshipFactory:

    @staticmethod
    def create(object_type, pos_x, pos_y, name = False):
        if not name:
            name = object_type
        match object_type:
            case "meteor":
                return Meteor(pos_x, pos_y, name)
            case "ship01":
                return Ship01(pos_x, pos_y, name)
        return False