class Info:
    def __init__(self, game):
        self.player = game.player
        self.screen = game.screen

    def display(self):
        self.screen.draw_image(10, 10, "assets/heart.png")
        self.screen.draw_text(45, 10, f"{self.player.spaceship.life}", 40, "red")