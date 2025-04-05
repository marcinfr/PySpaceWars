import timer

class SpaceObjectsManager:
    def __init__(self, game):
        self.space_objects = []
        self.screen = game.screen
        self.timer = timer.Timer()

    def add_object(self, space_object):
        self.space_objects.append(space_object)

    def display(self):
        for space_object in self.space_objects:
            space_object.display(self.screen)

    def process(self):
        elapsed_time = self.timer.elapsed_time()
        if elapsed_time == 0:
            return

        self.timer.set_time(0)
        enemies = []
        for space_object in self.space_objects:
            if not space_object.is_alive():
                self.space_objects.remove(space_object)

            if space_object.is_enemy:
                enemies.append(space_object)

        for space_object in self.space_objects:
            space_object.process(elapsed_time)
            if not space_object.is_enemy:
                for enemy in enemies:
                    if enemy.has_collision(space_object):
                        enemy.on_collision(space_object)

            if space_object.auto_shooting:
                space_object.shoot()