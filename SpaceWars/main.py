import screen
import background
import events
import menu

class Game:
    def __init__(self):
        self.screen = screen.Screen(1024, 768)
        self.events = events.Events()
        self.background = background.Background(self)
        self.menu = menu.Menu(self)
        self.running = True

    def move(self):
        if self.menu.is_displayed:
            return
        self.background.move()

    def display(self):
        self.background.display()
        self.menu.display()
        self.screen.display()

    def run(self):
        while not self.events.quit:
            self.events.collect()
            self.move()
            self.display()

game = Game()
game.run()