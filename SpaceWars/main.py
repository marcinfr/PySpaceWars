import screen
import background
import events
import menu
import stage
import spaceObjectsManager
import enemiesCreator

class Game:
    def __init__(self):
        self.screen = screen.Screen(1024, 768)
        self.events = events.Events()
        self.stage = stage.Stage()
        self.background = background.Background(self)
        self.menu = menu.Menu(self)
        self.space_objects_manager = spaceObjectsManager.SpaceObjectsManager(self)
        self.enemies_creator = enemiesCreator.EnemiesCreator(self)
        self.running = True

    def process(self):
        if self.menu.is_displayed:
            return
        self.enemies_creator.create()
        self.background.process()
        self.space_objects_manager.process()

    def display(self):
        self.background.display()
        self.space_objects_manager.display()
        self.menu.display()
        self.screen.display()

    def run(self):
        while not self.events.quit:
            self.events.collect()
            self.process()
            self.display()

game = Game()
game.run()