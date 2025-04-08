from datetime import datetime

class Timer:
    timers = {}
    is_paused = False
    paused_time = 0
    paused_on = 0

    def __init__(self):
        self.set_time("game")

    @staticmethod
    def get_timestamp():
        dt = datetime.now()
        return datetime.timestamp(dt)

    def tick(self):
        if self.is_paused:
            self.is_paused = False
            paused_time = self.get_timestamp() - self.paused_on
            for code in self.timers.keys():
                self.timers[code] += paused_time

    def pause(self):
        if not self.is_paused:
            self.is_paused = True
            self.paused_on = self.get_timestamp()

    def set_time(self, code):
        self.timers[code] = self.get_timestamp()

    def has_elapsed(self, code, seconds, reset_if_elapsed = True):
        if self.get_elapsed_time(code) < seconds:
            return False
        if reset_if_elapsed:
            self.set_time(code)
        return True

    def get_elapsed_time(self, code):
        time = self.timers.get(code)
        if not time:
            time = self.timers.get("game")
        return self.get_timestamp() - time
