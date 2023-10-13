import turtle
from Frog import Frog, FrogState
from BlockManager import BlockManager
from UI import UI
import math
from constants import screensize
from tkinter import PhotoImage

screen = turtle.Screen()

frog_image = PhotoImage(file="assets/turtle1.png").zoom(1, 1)
screen.addshape("frog_image", turtle.Shape("image", frog_image))
paused = True
is_game_over = False
screen.tracer(0)

def toggle_pause(x, y):
    global paused
    paused = not paused

def game_over():
    global is_game_over

    is_game_over = True
    UI.game_over()

def init_game():
    screen.setup(screensize[0], screensize[1])
    screen.onscreenclick(toggle_pause)

    render_tick()

    screen.onkeypress(frog.handle_input, 'w')

def render_tick():
    global paused

    if not paused and not is_game_over:
        frog.move()
        block_manager.move_blocks(frog)
        UI.draw()
        
        if frog.state == FrogState.PASSED:
            next_level()

        if frog.state == FrogState.CRASHED:
            game_over()
            block_manager.on_next_level() # just to reset

        screen.update()

    turtle.ontimer(render_tick, 20)

def next_level():
    frog._reset()
    block_manager.on_next_level()
    UI.add_score()
    

frog = Frog()
block_manager = BlockManager(blocks_amount=20)
UI = UI()
init_game()

screen.listen()
screen.mainloop()