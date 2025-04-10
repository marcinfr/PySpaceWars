import screen
from screen import Screen
import spaceObjectShape
import math

class AbstractObject:
    width = 40
    height = 40
    life = 1
    max_speed = 100
    speed_acceleration = 100
    collision_damage = 1
    img = False

    def __init__(self, pos_x, pos_y, name = "space_object"):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_enemy = True
        self.auto_shooting = False
        self.current_speed = 0
        self.current_speed_x = 0
        self.current_speed_y = 0
        self.speed = 0
        self.move_vector = [-2, 0]
        self.name = name
        self.controller = False
        self.orientation_x = 1
        self.shape = spaceObjectShape.Rectangle(self.width, self.height)

    def display(self, s:Screen):
        x1 = self.pos_x - self.width /2
        y1 = self.pos_y - self.height /2
        x2 = self.pos_x + self.width / 2
        y2 = self.pos_y + self.height / 2
        if self.img:
            rotation = 0
            if self.orientation_x < 0:
                rotation = 180
            s.draw_image(x1, y1, self.img, rotation)
        else:
            s.draw_rect_border(x1, y1, x2, y2, "red")

    def set_max_speed(self, as_current = False):
        self.speed = self.max_speed
        if as_current:
            self.current_speed_x = self.max_speed
            self.current_speed = self.speed

    def process(self, elapsed_time):
        if self.controller:
            self.controller.control(self)

        speed_acceleration = self.speed_acceleration * elapsed_time

        if self.speed > self.current_speed:
            self.current_speed += speed_acceleration
        elif self.speed < self.current_speed:
            self.current_speed -= speed_acceleration

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

        speed_x = 0
        speed_y = 0
        vector_length = math.sqrt(pow(self.move_vector[0], 2) + pow(self.move_vector[1], 2))
        if vector_length != 0:
            scale_factor = self.current_speed / vector_length
            speed_x = self.move_vector[0] * scale_factor
            speed_y = self.move_vector[1] * scale_factor

        if self.current_speed_x > speed_x:
            self.current_speed_x -= speed_acceleration
        elif self.current_speed_x < speed_x:
            self.current_speed_x += speed_acceleration

        if self.current_speed_y > speed_y:
            self.current_speed_y -= speed_acceleration
        elif self.current_speed_y < speed_y:
            self.current_speed_y += speed_acceleration

        self.pos_x += self.current_speed_x * elapsed_time
        self.pos_y += self.current_speed_y * elapsed_time

        if self.pos_x + self.width < 0:
            self.life = 0

        self.shape.set_position(self.pos_x - (self.width / 2), self.pos_y - (self.height / 2))

    def has_collision(self, space_object):
        return self.shape.has_collision(space_object.shape)

    def on_collision(self, space_object):
        space_object.life -= self.collision_damage
        self.life = 0

    def shoot(self):
        ...

    def is_alive(self):
        if self.life <= 0:
            return False
        return True