import random
from spaceObjects.spaceships.meteor import Meteor
import timer

class EnemiesCreator:
    def __init__(self, game):
        self.space_objects_manager = game.space_objects_manager
        self.stage = game.stage.stage
        self.screen = game.screen
        self.timer = timer.Timer()

    def create(self):
        if self.can_create():
            enemy = self.get_random_enemy()
            self.space_objects_manager.add_object(enemy)

    def can_create(self):
        if self.timer.has_elapsed():
            rand = random.randint(0, 400)
            if rand <= 1 + self.stage:
                return True
            self.timer.set_time(0.1)
        return False

    def get_random_enemy(self):
        x = self.screen.width
        y = random.randint(0, self.screen.height)
        enemy = Meteor(x, y)
        enemy.pos_x += enemy.width / 2
        enemy.set_max_speed()
        enemy.current_speed = enemy.speed
        return enemy