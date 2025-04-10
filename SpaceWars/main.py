from screen import Screen
from background import Background
from events import Events
from menu import Menu
from stage import Stage
from spaceObjectsManager import SpaceObjectsManager
from enemiesCreator import EnemiesCreator
from player import Player
from timer import Timer
from info import Info

class Game:
    def __init__(self):
        self.screen = Screen(1024, 768)
        self.timer = Timer()
        self.events = Events()
        self.stage = Stage()
        self.background = Background(self)
        self.menu = Menu(self)
        self.space_objects_manager = SpaceObjectsManager(self)
        self.enemies_creator = EnemiesCreator(self)
        self.player = Player(self)
        self.info = Info(self)
        self.running = True
        self.events.add_event("on_quit", self, "quit")

    def process(self):
        if self.menu.is_displayed:
            self.timer.pause()
            return
        self.timer.tick()
        self.enemies_creator.create()
        self.background.process()
        self.space_objects_manager.process()

    def display(self):
        self.background.display()
        self.space_objects_manager.display()
        self.menu.display()
        self.info.display()
        self.screen.display()

    def quit(self, event_data):
        self.running = False

    def run(self):
        while self.running:
            self.events.collect()
            self.process()
            self.display()

game = Game()
game.run()