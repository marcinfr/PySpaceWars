import pygame

class EventData:
    ...

class Events:
    key_esc = "esc"
    key_up = "up"
    key_down = "down"
    key_left = "left"
    key_right = "right"

    keys_map = {
        pygame.K_ESCAPE: key_esc,
        pygame.K_UP: key_up,
        pygame.K_DOWN: key_down,
        pygame.K_LEFT: key_left,
        pygame.K_RIGHT: key_right,
    }

    def __init__(self):
        self.events = {}

    def collect(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.dispatch("on_quit")
            elif event.type == pygame.KEYDOWN:
                self.dispatch_key(event.key, "down")
            elif event.type == pygame.KEYUP:
                self.dispatch_key(event.key, "up")

    def dispatch_key(self, key, suffix):
        key_code = self.keys_map.get(key)
        if not key_code:
            if key in range(0x110000):
                key_code = chr(key)
        if key_code:
            self.dispatch("on_" + key_code + "_key_" + suffix)
            data = EventData()
            data.key = key_code
            self.dispatch("on_key_" + suffix, data)

    def add_event(self, code, obj, method):
        if not code in self.events:
            self.events[code] = []
        self.events[code].append((obj, method))

    def dispatch(self, code, data = False):
        if not data:
            data = EventData()
        if code in self.events:
            for event in self.events[code]:
                getattr(event[0], event[1])(data)
