import pygame

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

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
        img = pygame.image.load(path)
        self.screen.blit(img, (x1, y1))

    def display(self, bg_color = "black"):
        pygame.display.flip()
        self.screen.fill(bg_color)

