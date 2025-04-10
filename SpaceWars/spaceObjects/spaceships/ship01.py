from spaceObjects.abstractObject import AbstractObject

class Ship01(AbstractObject):
    width = 77
    height = 66
    max_speed = 400
    speed_acceleration = 300
    collision_damage = 10
    img = "assets/spaceship01_77.png"