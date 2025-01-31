import pygame
from core import GetImage, assets, print_text, get_font, fonts, ImageButton

font_1 = get_font(fonts[0],40)
font_2 = get_font(fonts[0],30)
multiplayer_stack = ["home"]

# Objects
join_game = ImageButton(95,300,assets["Yellow"]["button_rectangle_depth_flat"],210,70,"Join Game",font_2,(7,7,7))
host_game = ImageButton(95,390,assets["Red"]["button_rectangle_depth_flat"],210,70,"Host Game",font_2,(7,7,7))

def draw_multiplayer_page(win):

    win.fill((51,153,218))

    page = multiplayer_stack[-1]

    # for Drawing multipayer home page
    if page == "home":

        # Title of page
        print_text(win,"Multiplayer\n    Zone",(255,255,255),100,60,font_1)

        # Buttons
        join_game.draw(win)
        host_game.draw(win)


def check_event_of_multiplayer_page(event):
    
    page = multiplayer_stack[-1]

    if page == "home":
        
        if join_game.is_clicked(event):
            print("Join game")
        elif host_game.is_clicked(event):
            print("Host game")