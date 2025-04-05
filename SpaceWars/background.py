import random
import timer

start_types = (
    # (speed, color)
    (4, (255, 255, 255)),
    (3, (120, 120, 120)),
    (2, (50, 50, 50))
)

class Star:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        type = random.choice(start_types)
        self.speed = type[0]
        self.color = type[1]

class Background:
    move_frequence = 0.05

    def __init__(self, screen, stars_amount = 100):
        self.timer = timer.Timer()
        self.timer.set_time(self.move_frequence)
        self.screen = screen
        self.stars = []
        for i in range(stars_amount):
            self.stars.append(
                Star(
                    random.randint(0, screen.width),
                    random.randint(0, screen.height)
                )
            )

    def draw(self):
        for star in self.stars:
            self.screen.draw_dot(star.x, star.y, star.color)

    def move(self):
        if not self.timer.has_elapsed():
            return

        self.timer.set_time(self.move_frequence)

        for star in self.stars:
            star.x -= star.speed
            if star.x < 0:
                star.x = self.screen.width
