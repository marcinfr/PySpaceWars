from spaceObjects.abstractObject import AbstractObject
from gunFactory import GunFactory

class Shooter(AbstractObject):

    def init(self):
        super().init()
        self.active_gun = ''
        self.guns = {}
        self.auto_shooting = True

    def process(self, elapsed_time):
        super().process(elapsed_time)
        if self.auto_shooting:
            self.shoot()

    def shoot(self, is_shooting = True):
        if is_shooting:
            self.is_shooting = is_shooting

    def get_bullets(self):
        gun = self.get_active_gun()
        if gun:
            bullets = gun.get_bullets(self.pos_x, self.pos_y)
            if not gun.is_shooting:
                self.is_shooting = False
            return bullets
        return []

    def add_gun(self, gun_code):
        if gun_code in self.guns:
            return
        gun = GunFactory.create(gun_code)
        gun.is_enemy = self.is_enemy
        print(f"{self.name}: {self.orientation_x}")
        gun.orientation_x = self.orientation_x
        if gun:
            self.guns[gun_code] = gun
            if not self.active_gun:
                self.active_gun = gun_code

    def get_active_gun(self):
        if self.active_gun in self.guns:
            return self.guns[self.active_gun]

    def set_active_gun(self, gun_code):
        if gun_code in self.guns:
            self.active_gun = gun_code