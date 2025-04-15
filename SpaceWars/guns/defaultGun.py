from timer import Timer
from bulletFactory import BulletFactory

class DefaultGun:
    cooldown = 2

    def __init__(self):
        self.is_shooting = False

    def get_bullets(self, x, y):
        if Timer.has_elapsed(id(self), self.cooldown):
            bullet = self.create_bullet("default", x, y)
            if bullet:
                return [bullet]
        return []

    def create_bullet(self, bullet_type, x, y):
        bullet = BulletFactory.create(bullet_type)
        bullet.pos_x = x
        bullet.pos_y = y
        bullet.is_enemy = self.is_enemy;
        bullet.move_vector[0] = self.orientation_x
        bullet.orientation_x = self.orientation_x
        bullet.set_max_speed(True)
        return bullet