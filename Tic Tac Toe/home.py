# import usefull modules
import pygame

from core import ImageButton,get_font,fonts,assets,white,stack,red,green

# Initilize pygame
pygame.init()

# Objects
two_play_button = ImageButton(95, 265, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Player",get_font(fonts[0],25),white)
com_play_button = ImageButton(95, 345, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Computer",get_font(fonts[0],25),white)
online_play_button = ImageButton(95, 425, assets["Green"]["button_rectangle_depth_flat"],210,70,"Online Play",get_font(fonts[0],25),white)

# Variables
demo_game_grid = {(i, j): None for i in range(3) for j in range(3)}
demo_game_grid = {(0,0):None,(0,1):"O",(0,2):"X",
                  (1,0):"X",(1,1):None,(1,2):"O",
                  (2,0):"O",(2,1):"X",(2,2):None}
start_ticks = pygame.time.get_ticks()

# For Draw O
def draw_O(win,x,y,width):
    radius = width//2
    center = (x+radius,y+radius)
    pygame.draw.circle(win,green,center,radius-5,6)

# For Draw X
def draw_X(win,x,y,width):
    pygame.draw.line(win,red,(x+10,y+10),(x+width-10,y+width-10),7)
    pygame.draw.line(win,red,(x+10,y+width-10),(x+width-10,y+10),7)

# Animation for demo screen
def animation_of_demo():
    # Introduce 5 seconds delay before starting
    current_ticks = pygame.time.get_ticks()
    if current_ticks - start_ticks < 5000:
        

        start_ticks = pygame.time.get_ticks()

# For Draw Homepage
def draw_home_page(win):
    win.fill((51, 153, 218))

    two_play_button.draw(win)
    com_play_button.draw(win)
    online_play_button.draw(win)

    for i in range(1,3):
        # For Horizontal lines
        pygame.draw.line(win,white,(95,(70*i)+30),(305,(70*i)+30),6)
        pygame.draw.circle(win,white,(95,(70*i)+31),3)
        pygame.draw.circle(win,white,(305,(70*i)+31),3)

        # For Vertical lines
        pygame.draw.line(win,white,((70*i)+95,30),((70*i)+95,240),6)
        pygame.draw.circle(win,white,((70*i)+96,30),3)
        pygame.draw.circle(win,white,((70*i)+96,240),3)

    for i in demo_game_grid:
        
        # Position for each O and X in cordinate (x,y)
        x = (i[0]*70)+100
        y = (i[1]*70)+33

        # For drawing X or O on screen
        if demo_game_grid[i] == "O":
            draw_O(win,x,y,65)
        elif demo_game_grid[i] == "X":
            draw_X(win,x,y,65)

# For check home page event
def check_event_of_home_page(event):
    
    if two_play_button.is_clicked(event):
        stack.append("gamepage")

    elif com_play_button.is_clicked(event):
        print("vscomgame")

    elif online_play_button.is_clicked(event):
        print("online")

if __name__ == "__main__":
    pass