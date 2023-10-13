import turtle
from constants import screensize

class UI(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.ht()
        self.color('black')
        self.setpos(-screensize[0] / 2.8, screensize[1] / 2.3)
    
    def draw(self):
        self.clear()
        self.write(f'Level: {self.score}', align="center", font=('Comic Sans', 20, 'normal'))

    def add_score(self):
        self.score += 1
        
    def game_over(self):
        self.clear()
        self.setpos(0, screensize[1] / 3)
        self.write('GAME OVER', align="center", font=('Comic Sans', 30, 'normal'))
        self.setpos(0, screensize[1] / 5)
        self.write(f'Final score: {self.score}', align="center", font=('Comic Sans', 20, 'normal'))