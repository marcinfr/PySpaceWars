import screen
import background
import events
import menu
import stage
import spaceObjectsManager
import enemiesCreator
import player

class Game:
    def __init__(self):
        self.screen = screen.Screen(1024, 768)
        self.events = events.Events()
        self.stage = stage.Stage()
        self.background = background.Background(self)
        self.menu = menu.Menu(self)
        self.space_objects_manager = spaceObjectsManager.SpaceObjectsManager(self)
        self.enemies_creator = enemiesCreator.EnemiesCreator(self)
        self.player = player.Player(self)
        self.running = True
        self.events.add_event("on_quit", self, "quit")

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

    def quit(self):
        self.running = False

    def run(self):
        while self.running:
            self.events.collect()
            self.process()
            self.display()

game = Game()
game.run()