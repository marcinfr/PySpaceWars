import random
import timer

start_types = (
    # (speed, color)
    (40, (255, 255, 255)),
    (30, (120, 120, 120)),
    (20, (50, 50, 50))
)

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        type = random.choice(start_types)
        self.speed = type[0]
        self.color = type[1]

class Background:
    def __init__(self, game, stars_amount = 100):
        self.timer = timer.Timer()
        self.screen = game.screen
        self.stars = []
        for i in range(stars_amount):
            self.stars.append(
                Star(
                    random.randint(0, self.screen.width),
                    random.randint(0, self.screen.height)
                )
            )

    def display(self):
        for star in self.stars:
            self.screen.draw_dot(star.x, star.y, star.color)

    def process(self):
        elapsed_time = self.timer.get_elapsed_time("stars")
        self.timer.set_time("stars")

        for star in self.stars:
            star.x -= star.speed * elapsed_time
            if star.x < 0:
                star.x = self.screen.width
