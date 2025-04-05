import random
import spaceObjects.enemies.meteor as meteor
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
        if (self.timer.has_elapsed()
                and random.randint(0, 100) <= 1 + self.stage):
            self.timer.set_time(10)
            return True
        return False

    def get_random_enemy(self):
        x = self.screen.width
        y = random.randint(0, self.screen.height)
        enemy = meteor.Meteor(x, y)
        enemy.pos_x += enemy.width / 2
        enemy.set_max_speed()
        return enemy