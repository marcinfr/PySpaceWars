import pygame

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

    def draw_dot(self, x, y, color):
        pygame.draw.circle(self.screen, color, pygame.Vector2(x, y), 1)

    def display(self):
        pygame.display.flip()
        self.screen.fill("black")

