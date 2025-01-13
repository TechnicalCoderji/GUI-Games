# module for Game Page
import pygame
from random import choice

from core import GetImage,WIDTH,HEIGHT,assets,red,green,white,print_text,get_font,fonts,ImageButton,stack

# Initilize pygame
pygame.init()

# variables
game_grids = {(i, j): None for i in range(3) for j in range(3)}
move_count = choice([0,1])
game_state = "running"

# Define a color with an alpha value (RGBA)
transparent_color = (0, 0, 0, 150)  # Green with 50% transparency

# Create a surface with transparency
transparent_surface = pygame.Surface((WIDTH,HEIGHT), pygame.SRCALPHA)
transparent_surface.fill(transparent_color)

# Define the possible winning combinations
winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

# IMAGES
pause_bg = GetImage((20,215,360,120),assets["Yellow"]["button_rectangle_border"])

# Buttons
home_button = ImageButton(50,280,assets["Blue"]["button_rectangle_depth_flat"],90,30,"Home",get_font(fonts[0],17),(0,0,0))

restart_button = ImageButton(155,280,assets["Green"]["button_rectangle_depth_flat"],90,30,"Restart",get_font(fonts[0],17),(0,0,0))

continue_button = ImageButton(260,280,assets["Yellow"]["button_rectangle_depth_flat"],90,30,"Continue",get_font(fonts[0],17),(0,0,0))

pause_button = ImageButton(20,470,assets["Yellow"]["button_square_depth_flat"],60,60,"| |",get_font(fonts[0],30),(0,0,0))

home_1_button = ImageButton(90,280,assets["Blue"]["button_rectangle_depth_flat"],90,30,"Home",get_font(fonts[0],17),(0,0,0))

replay_button = ImageButton(220,280,assets["Green"]["button_rectangle_depth_flat"],90,30,"Replay",get_font(fonts[0],17),(0,0,0))

# For Draw O
def draw_O(win,x,y,width):
    radius = width//2
    center = (x+radius,y+radius)
    pygame.draw.circle(win,(0,0,255),center,radius-5,10)

# For Draw X
def draw_X(win,x,y,width):
    pygame.draw.line(win,red,(x+10,y+10),(x+width-10,y+width-10),13)
    pygame.draw.line(win,red,(x+10,y+width-10),(x+width-10,y+10),13)

# For restarting game
def game_restart():
    global move_count, game_grids

    move_count = choice([0,1])
    game_grids = {(i, j): None for i in range(3) for j in range(3)}

# Function for cheking winner of game
def check_winner():
    
    # Check for a winner
    for combination in winning_combinations:
        values = [game_grids[pos] for pos in combination]
        if values[0] is not None and values.count(values[0]) == len(values):
            return values[0]  # Return the player ('X' or 'O')

    # Check for a tie
    if all(value is not None for value in game_grids.values()):
        return "Tie"

    # If there's no winner or tie, return None
    return None

# For stop game
def draw_pause_menu(win):
    global game_state
    winner = check_winner()
    game_state = "win" if check_winner() else "running" if game_state!="pause" else "pause"

    if game_state != "running":
        win.blit(transparent_surface,(0,0))
        pause_bg.draw(win)

        if game_state == "pause":
            print_text(win,"Pause",(0,0,0),145,237,get_font(fonts[0],35))

            home_button.draw(win)
            restart_button.draw(win)
            continue_button.draw(win)

        if game_state == "win":
            if winner == "Tie":
                print_text(win,"Tie",(0,0,0),175,237,get_font(fonts[0],35))
            else:
                print_text(win,winner+" Win the Game",(0,0,0),65,237,get_font(fonts[0],35))

            home_1_button.draw(win)
            replay_button.draw(win)

# For check game page event
def check_event_of_game_page(event):
    global game_state,stack,move_count
    
    # For mouse button down check
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if game_state == "running":
            player = "O" if move_count%2==0 else "X"
            for i,j in game_grids:
                if not game_grids[(i,j)]:
                    rect = pygame.rect.Rect(i*120+31,j*120+31,100,100)
                    if rect.collidepoint(x,y):
                        game_grids[(i,j)] = player
                        move_count += 1
                        break
            if pause_button.is_clicked(event):
                game_state = "pause"
    
        elif game_state == "pause":
            if home_button.is_clicked(event):
                stack.pop()
                game_restart()
                game_state = "running"

            elif restart_button.is_clicked(event):
                game_restart()
                game_state = "running"

            elif continue_button.is_clicked(event):
                game_state = "running"

        elif game_state == "win":
            if home_1_button.is_clicked(event):
                stack.pop()
                game_restart()
                game_state = "running"

            elif replay_button.is_clicked(event):
                game_restart()
                game_state = "running"

# For Draw Main Game Page
def draw_game_page(win):
    win.fill((51,153,218))

    for i in range(1,3):
        # For Horizontal lines
        pygame.draw.line(win,white,(20,(120*i)+20),(380,(120*i)+20),10)
        pygame.draw.circle(win,white,(20,(120*i)+21),5)
        pygame.draw.circle(win,white,(380,(120*i)+21),5)

        # For Vertical lines
        pygame.draw.line(win,white,((120*i)+20,20),((120*i)+20,380),10)
        pygame.draw.circle(win,white,((120*i)+21,20),5)
        pygame.draw.circle(win,white,((120*i)+21,380),5)

    for i in game_grids:
        
        # Position for each O and X in cordinate (x,y)
        x = (i[0]*120)+31
        y = (i[1]*120)+31

        # For drawing X or O on screen
        if game_grids[i] == "O":
            draw_O(win,x,y,100)
        elif game_grids[i] == "X":
            draw_X(win,x,y,100)

    pygame.draw.rect(win,(100,100,100),(0,400,WIDTH,150))
    pause_button.draw(win)

    if game_state != "win":
        text_to_blit = "O's move" if move_count%2==0 else "X's move"
        print_text(win,text_to_blit,white,130,480,get_font(fonts[0],50))

    draw_pause_menu(win)

if __name__ == "__main__":
    pass