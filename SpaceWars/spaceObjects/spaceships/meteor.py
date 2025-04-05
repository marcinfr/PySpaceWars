from spaceObjects.abstractObject import AbstractObject

class Meteor(AbstractObject):
    def on_collision(self, space_object):
        space_object.life = 0