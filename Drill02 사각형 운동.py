from pico2d import *

open_canvas()

# fill here

close_canvas()

import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
num = 1
while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    if(num ==1):
        x = math.cos(x)
    delay(0.01)

close_canvas()
