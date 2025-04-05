from spaceObjects.spaceships.meteor import Meteor

class Player:
    def __init__(self, game):
        self.events = game.events
        pos_x = 1
        pos_y = game.screen.height / 2
        self.spaceship = Meteor(pos_x, pos_y,  "Player")
        self.spaceship.move_vector = [0, 0]
        self.spaceship.life = 100
        self.spaceship.controller = self
        self.x_move_direction = 0
        self.y_move_direction = 0
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        game.space_objects_manager.add_object(self.spaceship)
        self.events.add_event("on_key_up", self, "on_key_up")
        self.events.add_event("on_key_down", self, "on_key_down")

    def control(self, spaceship):
        if self.moving_up:
            self.y_move_direction = -1
        if self.moving_down:
            self.y_move_direction = 1
        if self.moving_left:
            self.x_move_direction = -1
        if self.moving_right:
            self.x_move_direction = 1

        if self.moving_up or self.moving_down or self.moving_left or self.moving_right:
            spaceship.set_max_speed()
        else:
            spaceship.speed = 0

        spaceship.move_vector = [self.x_move_direction, self.y_move_direction]

    def on_key_down(self, data):
        match data.key:
            case self.events.key_up:
                self.moving_up = True
                self.y_move_direction = -1
                return
            case self.events.key_down:
                self.moving_down = True
                return
            case self.events.key_left:
                self.moving_left = True
                return
            case self.events.key_right:
                self.moving_right = True
                return

    def on_key_up(self, data):
        match data.key:
            case self.events.key_up:
                self.moving_up = False
                self.y_move_direction = 0
                return
            case self.events.key_down:
                self.moving_down = False
                self.y_move_direction = 0
                return
            case self.events.key_left:
                self.moving_left = False
                self.x_move_direction = 0
                return
            case self.events.key_right:
                self.moving_right = False
                self.x_move_direction = 0
                return

