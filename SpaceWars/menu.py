class Menu:
    def __init__(self, game):
        self.screen = game.screen
        self.events = game.events
        self.is_displayed = False

    def display(self, width = 400, height = 600):
        if self.events.is_key_just_pressed(self.events.escKey):
            self.is_displayed = not self.is_displayed

        if not self.is_displayed:
            return

        center_x = self.screen.width / 2
        center_y = self.screen.height / 2
        x1 = int(center_x - width / 2)
        y1 = int(center_y - height / 2)
        x2 = int(center_x + width / 2)
        y2 = int(center_y + height / 2)

        self.screen.draw_rectangle(x1, y1, x2, y2, "black", 200)
        self.screen.draw_rect_border(x1, y1, x2, y2, "white")