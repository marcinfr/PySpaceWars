import random
from spaceshipFactory import SpaceshipFactory
from gunFactory import GunFactory

class EnemiesCreator:
    def __init__(self, game):
        self.space_objects_manager = game.space_objects_manager
        self.stage = game.stage.stage
        self.screen = game.screen
        self.timer = game.timer

    def create(self):
        if self.can_create():
            enemy = self.get_random_enemy()
            if enemy:
                self.space_objects_manager.add_object(enemy)

    def can_create(self):
        if self.timer.has_elapsed("enemies_creator_timer", 1):
            rand = random.randint(0, 10)
            if rand <= 1 + self.stage:
                return True
        return False

    def get_random_enemy(self):
        x = self.screen.width
        y = random.randint(0, self.screen.height)
        rand = random.randint(0, 4)
        if rand < 2:
            spaceship_type = "meteor"
            gun_type = False
        else:
            spaceship_type = "ship01"
            gun_type = "default"

        enemy = SpaceshipFactory.create(spaceship_type, x, y)

        if enemy:
            enemy.pos_x += enemy.width / 2
            enemy.set_max_speed(True)
            enemy.orientation_x = -1
            if gun_type:
                enemy.add_gun(gun_type)
        return enemy