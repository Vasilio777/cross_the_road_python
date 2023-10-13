import turtle
from constants import screensize, cell_size
from enum import Enum

class FrogState(Enum):
    MOVING = 1
    PASSED = 2
    CRASHED = 3

class Frog(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.is_move_requested = False
        self.up()
        self.shape('frog_image')
        self.left(90)
        self.max_x = screensize[0] / 2
        self.max_y = screensize[1] / 2
        self.state = FrogState.MOVING
        self._reset()

    def handle_input(self):
        self.is_move_requested = True

    def _reset(self):
        self.setpos(0, -self.max_y + cell_size)
        self.state = FrogState.MOVING

    def move(self):
        if self.is_move_requested:
            self.is_move_requested = False
            self.forward(cell_size)

            if self.ycor() >= self.max_y:
                self.state = FrogState.PASSED

    def crash(self):
        self.state = FrogState.CRASHED