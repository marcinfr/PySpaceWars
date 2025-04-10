class SpaceObjectShape:
    def __init__(self):
        ...

class Rectangle(SpaceObjectShape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.pos_x = self.pos_x2 = None
        self.pos_y = self.pos_y2 = None

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y
        self.pos_x2 = x + self.width
        self.pos_y2 = y + self.height

    def has_collision(self, shape):

        if self.pos_x is None:
            return False

        if shape.pos_x is None:
            return False

        if shape.pos_x2 < self.pos_x:
            return False

        if shape.pos_x > self.pos_x2:
            return False

        if shape.pos_y2 < self.pos_y:
            return False

        if shape.pos_y > self.pos_y2:
            return False

        return True