class Menu:
    def __init__(self, game):
        self.screen = game.screen
        game.events.add_event("on_esc_key_down", self, "toggle_menu")
        self.is_displayed = False

    def toggle_menu(self):
        self.is_displayed = not self.is_displayed

    def display(self, width = 400, height = 600):
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