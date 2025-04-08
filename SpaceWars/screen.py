import pygame

class Screen:
    images = {}

    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def draw_dot(self, x, y, color):
        pygame.draw.circle(self.screen, color, (x, y), 1)

    def draw_rectangle(self, x1, y1, x2, y2, color, alfa = 255):
        color = pygame.Color(color)
        color.a = alfa
        rect = pygame.Surface((x2 - x1, y2 - y1), pygame.SRCALPHA)
        rect.fill(color)
        self.screen.blit(rect, (x1, y1))

    def draw_rect_border(self, x1, y1, x2, y2, color):
        pygame.draw.line(self.screen, color, (x1, y1), (x2, y1))
        pygame.draw.line(self.screen, color, (x2, y1), (x2, y2))
        pygame.draw.line(self.screen, color, (x2, y2), (x1, y2))
        pygame.draw.line(self.screen, color, (x1, y2), (x1, y1))

    def draw_image(self, x1, y1, path):
        img = self.images.get(path)
        if not img:
            img = pygame.image.load(path)
            self.images[path] = img
        self.screen.blit(img, (x1, y1))

    def draw_text(self, x, y, text, color):
        font = pygame.font.SysFont(pygame.font.get_default_font(), 25)
        text = font.render(text, True, color)
        self.screen.blit(text, (x, y))

    def display(self, bg_color = "black"):
        self.clock.tick()
        self.draw_text(self.width - 80, self.height - 25,f"{int(self.clock.get_fps())} fps", (255, 255, 255))
        pygame.display.flip()
        self.screen.fill(bg_color)

