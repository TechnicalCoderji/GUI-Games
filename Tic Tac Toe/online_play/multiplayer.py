import pygame
from core import assets, print_text, get_font, fonts, ImageButton, TextInputBox

# For Multiplayer Game
from .ip_get import get_ip
from _thread import start_new_thread
from .network import Network
from .Server import start_server

# Variables
font_1 = get_font(fonts[0],40)
font_2 = get_font(fonts[0],30)
font_3 = get_font(fonts[0],20)
multiplayer_stack = ["home"]
server_IP_address = get_ip()

# Network Variables
network_object = None
player = None
game = None

# Objects
join_game = ImageButton(95,300,assets["Yellow"]["button_rectangle_depth_flat"],210,70,"Join Game",font_2,(7,7,7))
host_game = ImageButton(95,390,assets["Red"]["button_rectangle_depth_flat"],210,70,"Host Game",font_2,(7,7,7))
input_box = TextInputBox(75,100,250,30,font_3)
join_button = ImageButton(95,150,assets["Yellow"]["button_rectangle_depth_flat"],210,70,"Join Game",font_2,(7,7,7))

def draw_multiplayer_page(win):
    global game, network_object

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
        
        print_text(win, "Host Server IP", (255,255,255), 100,60,font_2)
        print_text(win, server_IP_address, (255,255,255), 100,120,font_2)

        game = network_object.send("get")
        if game.connected():
            multiplayer_stack.append("game")
        else:
            print_text(win, "Wating For Player", (0,255,0), 100,320,font_2)

    elif page == "game":
        pass

def check_event_of_multiplayer_page(event):
    global multiplayer_stack, network_object, player
    
    page = multiplayer_stack[-1]

    if page == "home":
        
        if join_game.is_clicked(event):
            multiplayer_stack.append("join")

        elif host_game.is_clicked(event):

            # Create Server for Host the Game
            start_new_thread(start_server,(server_IP_address,))

            # Create Network Object for Deal With Server
            network_object = Network(server_IP_address)
            player = network_object.get_p()
            print(player)

            multiplayer_stack.append("host")

    elif page == "join":
        
        input_box.handle_event(event)

        if join_button.is_clicked(event):
            print(input_box.text)

            # Create Network Object for Deal With Server
            network_object = Network(server_IP_address)
            player = network_object.get_p()
            print(player)

            multiplayer_stack.append("Game")

    elif page == "host":
        pass

    elif page == "game":
        pass