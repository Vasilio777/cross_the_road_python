import turtle
import random 
from constants import screensize, cell_size

class MovingBlock(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.shape_width = 50
        self.max_x = screensize[0] / 1.5
        self.max_y = screensize[1] / 2 - cell_size*2
        self.step_size_default = 10
        self.step_size = self.step_size_default
        self.speed = 1
        self.up()
        self.shape('square')
        self.shapesize(1, self.shape_width / 10, 0)
        self.right(180)

        self.is_active = False
        self._reset(0)


    def _reset(self, speed_offset):
        self.color(random.random(), random.random(), random.random())
        self.setpos(self.max_x, random.randrange(-self.max_y, self.max_y,  cell_size))
        self.speed += speed_offset
        self.step_size = self.step_size_default * self.speed

    def move(self, frog):
        if self.is_active:
            self.forward(self.step_size)
            if self.xcor() < -self.max_x:
                self._reset(0)
            
            frog_pos = frog.pos()
            if int(self.ycor()) == int(frog_pos[1]) and self.distance(frog.pos()) < self.shape_width:
                frog.crash()

    def set_active(self, in_active):
        self.is_active = in_active