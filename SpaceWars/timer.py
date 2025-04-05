from datetime import datetime

class Timer:
    def __init__(self):
        self.start_time = 0
        self.time = 0

    @staticmethod
    def get_timestamp():
        dt = datetime.now()
        return int(datetime.timestamp(dt) * 1000)

    def set_time(self, seconds):
        self.start_time = self.get_timestamp()
        self.time = seconds * 1000

    def has_elapsed(self):
        if self.start_time > 0:
            if self.start_time < self.get_timestamp() - self.time:
                return True
            return False
        return True
