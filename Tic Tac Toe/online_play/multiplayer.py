import pygame
from core import GetImage, assets, print_text, get_font, fonts, ImageButton, TextInputBox
from .ip_get import get_ip

# Variables
font_1 = get_font(fonts[0],40)
font_2 = get_font(fonts[0],30)
font_3 = get_font(fonts[0],20)
multiplayer_stack = ["home"]
server_IP_address = get_ip()

# Objects
join_game = ImageButton(95,300,assets["Yellow"]["button_rectangle_depth_flat"],210,70,"Join Game",font_2,(7,7,7))
host_game = ImageButton(95,390,assets["Red"]["button_rectangle_depth_flat"],210,70,"Host Game",font_2,(7,7,7))
input_box = TextInputBox(75,100,250,30,font_3)
join_button = ImageButton(95,150,assets["Yellow"]["button_rectangle_depth_flat"],210,70,"Join Game",font_2,(7,7,7))

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

    elif page == "join":
        
        print_text(win,"Enter Host Server IP",(255,255,255),55,60,font_2)

        input_box.draw(win)
        input_box.update()

        join_button.draw(win)

    elif page == "host":
        
        print_text(win, server_IP_address, (255,255,255), 55,60,font_2)

def check_event_of_multiplayer_page(event):
    global multiplayer_stack
    
    page = multiplayer_stack[-1]

    if page == "home":
        
        if join_game.is_clicked(event):
            multiplayer_stack.append("join")
        elif host_game.is_clicked(event):
            multiplayer_stack.append("host")

    elif page == "join":
        
        input_box.handle_event(event)

        if join_button.is_clicked(event):
            print(input_box.text)

    elif page == "host":
        pass
