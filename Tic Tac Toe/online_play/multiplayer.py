import pygame
from core import assets, print_text, get_font, fonts, ImageButton, TextInputBox, WIDTH, HEIGHT, GetImage

# For Multiplayer Game
from .ip_get import get_ip
from _thread import start_new_thread
from .network import Network
from .Server import start_server

# Variables
font_1 = get_font(fonts[0],40)
font_1_5 = get_font(fonts[0],35)
font_2 = get_font(fonts[0],30)
font_3 = get_font(fonts[0],20)
multiplayer_stack = ["home"]
server_IP_address = get_ip()
game_state = "running"

# Network Variables
network_object = None
player = None
game = None

# IMAGES
pause_bg = GetImage((20,215,360,120),assets["Yellow"]["button_rectangle_border"])

# Define a color with an alpha value (RGBA)
transparent_color = (0, 0, 0, 150)  # Green with 50% transparency

# Create a surface with transparency
transparent_surface = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
transparent_surface.fill(transparent_color)

# Objects
join_game = ImageButton(95,300,assets["Yellow"]["button_rectangle_depth_flat"],210,70,"Join Game",font_2,(7,7,7))

host_game = ImageButton(95,390,assets["Red"]["button_rectangle_depth_flat"],210,70,"Host Game",font_2,(7,7,7))

input_box = TextInputBox(75,100,250,30,font_3)

join_button = ImageButton(95,150,assets["Yellow"]["button_rectangle_depth_flat"],210,70,"Join Game",font_2,(7,7,7))

pause_button = ImageButton(20,470,assets["Yellow"]["button_square_depth_flat"],60,60,"| |",get_font(fonts[0],30),(0,0,0))

# Buttons
home_button = ImageButton(90,280,assets["Blue"]["button_rectangle_depth_flat"],90,30,"Home",get_font(fonts[0],17),(0,0,0))

continue_button = ImageButton(220,280,assets["Yellow"]["button_rectangle_depth_flat"],90,30,"Continue",get_font(fonts[0],17),(0,0,0))

replay_button = ImageButton(220,280,assets["Green"]["button_rectangle_depth_flat"],90,30,"Replay",get_font(fonts[0],17),(0,0,0))

# Functions
# For Draw O
def draw_O(win,x,y,width):
    radius = width//2
    center = (x+radius,y+radius)
    pygame.draw.circle(win,(0,0,255),center,radius-5,10)

# For Draw X
def draw_X(win,x,y,width):
    pygame.draw.line(win,(255,0,0),(x+10,y+10),(x+width-10,y+width-10),13)
    pygame.draw.line(win,(255,0,0),(x+10,y+width-10),(x+width-10,y+10),13)

# Function for back to home
def go_home():
    global network_object,player

    while multiplayer_stack[-1] != "home":
        multiplayer_stack.pop()
    
    network_object = None
    player = None

# For convert tuple to string 
tuple_to_string = lambda x,y : f"{x}{y}"

# For handle event of game page
def handle_event_of_game_page(event):
    global game_state, player, game, network_object
    
    # For mouse button down check
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if game_state == "running":
            
            if game.turn == player:
                for i,j in game.board:
                    if not game.board[(i,j)]:
                        rect = pygame.rect.Rect(i*120+31,j*120+31,100,100)
                        if rect.collidepoint(x,y):
                            game = network_object.send(tuple_to_string(i,j))
                            break
            if pause_button.is_clicked(event):
                game_state = "pause"
    
        elif game_state == "pause":
            if home_button.is_clicked(event):
                game = network_object.send("leave")
                go_home()

            elif continue_button.is_clicked(event):
                game_state = "running"

        elif game_state == "win":
            if home_button.is_clicked(event):
                game = network_object.send("leave")
                go_home()

            elif replay_button.is_clicked(event):
                game = network_object.send("reset")
                game_state = "running"

# For Drawing Pause Menu
def draw_pause_menu(win):
    global game_state
    winner = game.winner()
    game_state = "win" if winner else "running" if game_state!="pause" else "pause"

    if game_state != "running":
        win.blit(transparent_surface,(0,0))
        pause_bg.draw(win)

        if game_state == "pause":
            print_text(win,"Pause",(0,0,0),145,237,get_font(fonts[0],35))

            home_button.draw(win)
            continue_button.draw(win)

        if game_state == "win":
            text_message = "You Win The Game" if winner == player else "You Lose The Game"
            if winner == "Tie":
                print_text(win,"Tie",(0,0,0),175,237,get_font(fonts[0],35))
            else:
                print_text(win,text_message,(0,0,0),60,237,get_font(fonts[0],30))

            home_button.draw(win)
            replay_button.draw(win)

# For Drawing Game Page
def draw_game_page(win):
    global game

    for i in range(1,3):
        # For Horizontal lines
        pygame.draw.line(win,(255,255,255),(20,(120*i)+20),(380,(120*i)+20),10)
        pygame.draw.circle(win,(255,255,255),(20,(120*i)+21),5)
        pygame.draw.circle(win,(255,255,255),(380,(120*i)+21),5)

        # For Vertical lines
        pygame.draw.line(win,(255,255,255),((120*i)+20,20),((120*i)+20,380),10)
        pygame.draw.circle(win,(255,255,255),((120*i)+21,20),5)
        pygame.draw.circle(win,(255,255,255),((120*i)+21,380),5)

    game = network_object.send("get")

    if not game:
        go_home()
    else:
        for i in game.board:
            
            # Position for each O and X in cordinate (x,y)
            x = (i[0]*120)+31
            y = (i[1]*120)+31

            # For drawing X or O on screen
            if game.board[i] == "O":
                draw_O(win,x,y,100)
            elif game.board[i] == "X":
                draw_X(win,x,y,100)

        pygame.draw.rect(win,(100,100,100),(0,400,WIDTH,150))
        pause_button.draw(win)

        if game_state != "win":
            text_to_blit = "Your Move" if game.turn == player else "Oppenent's Move"
            print_text(win,f"You Are {player}",(255,255,255),100,430,font_1_5)
            print_text(win,text_to_blit,(255,255,255),100,490,font_1_5)

        draw_pause_menu(win)

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
        print_text(win, "Wating For Player", (0,255,0), 100,320,font_2)

        game = network_object.send("get")
        if game.connected():
            multiplayer_stack.append("game")
        
    elif page == "game":
        draw_game_page(win)

def check_event_of_multiplayer_page(event):
    global multiplayer_stack, network_object, player, game
    
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

            # For Game Object
            game = network_object.send("get")
            multiplayer_stack.append("game")

    elif page == "host":
        pass

    elif page == "game":
        if not game.leave:
            handle_event_of_game_page(event)
        else:
            go_home()