# import usefull modules
import pygame

from core import ImageButton,get_font,fonts,assets,white,stack
from game import timer_10_sec

# Objects
two_play_button = ImageButton(95, 265, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Player",get_font(fonts[0],25),white)
com_play_button = ImageButton(95, 345, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Computer",get_font(fonts[0],25),white)
online_play_button = ImageButton(95, 425, assets["Green"]["button_rectangle_depth_flat"],210,70,"Online Play",get_font(fonts[0],25),white)

# For Draw Homepage
def draw_home_page(win):
    win.fill((51, 153, 218))

    two_play_button.draw(win)
    com_play_button.draw(win)
    online_play_button.draw(win)

# For check home page event
def check_event_of_home_page(event):
    
    if two_play_button.is_clicked(event):
        stack.append("gamepage")
        timer_10_sec.restart()

    elif com_play_button.is_clicked(event):
        print("vscomgame")

    elif online_play_button.is_clicked(event):
        print("online")

if __name__ == "__main__":
    pass