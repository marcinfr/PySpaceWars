from spaceObjects.abstractObject import AbstractObject

class DefaultBullet(AbstractObject):
    width = 30
    height = 1
    max_speed = 600
    collision_damage = 5