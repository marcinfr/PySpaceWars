from spaceObjects.abstractObject import AbstractObject
from screen import Screen

class Meteor(AbstractObject):
    width = 184
    height = 159
    img = "assets/meteor_184.png"

    def on_collision(self, space_object):
        space_object.life = 0
