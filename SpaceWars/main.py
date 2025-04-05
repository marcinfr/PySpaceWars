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

    def run(self):
        while not self.events.quit:
            self.events.collect()

            if not self.menu.display:
                self.background.move()

            self.background.draw()
            self.screen.display()
            if self.events.is_key_just_pressed(self.events.escKey):
                self.menu.display = not self.menu.display

            if self.events.is_key_pressed("a"):
                print("a")

game = Game()
game.run()