from spaceObjects.abstractObject import AbstractObject

class Meteor(AbstractObject):
    max_speed = 2

    def on_collision(self, space_object):
        space_object.life = 0