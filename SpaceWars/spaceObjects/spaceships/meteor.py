from spaceObjects.abstractObject import AbstractObject
from screen import Screen

class Meteor(AbstractObject):
    width = 184
    height = 159

    def on_collision(self, space_object):
        space_object.life = 0

    def display(self, s: Screen):
        x1 = self.pos_x - self.width / 2
        y1 = self.pos_y - self.height / 2
        x2 = self.pos_x + self.width / 2
        y2 = self.pos_y + self.height / 2
        s.draw_image(x1, y1, "assets/meteor_184.png")