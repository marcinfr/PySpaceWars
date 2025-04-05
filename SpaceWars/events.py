import pygame

class Events:
    escKey = pygame.K_ESCAPE

    def __init__(self):
        self.quit = False
        self.keys_pressed = []

    def collect(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
            elif (event.type == pygame.KEYDOWN
                  and not event.key in self.keys_pressed):
                self.keys_pressed.append(event.key)
            elif (event.type == pygame.KEYUP
                  and event.key in self.keys_pressed):
                self.keys_pressed.remove(event.key)

    def is_key_pressed(self, key):
        if type(key) == str:
            key = ord(key)

        if key in self.keys_pressed:
            return True
        return False