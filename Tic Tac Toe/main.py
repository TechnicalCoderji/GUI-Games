# import usefull modules
import pygame

from core import RES,stack
from game import draw_game_page,check_event_of_game_page
from home import draw_home_page,check_event_of_home_page
from computer import draw_com_page,check_event_of_com_page
from online_play.multiplayer import draw_multiplayer_page,check_event_of_multiplayer_page

# a function that initializes all imported Pygame modules
pygame.init()

# Creating window
win = pygame.display.set_mode(RES) # make screen/window object
pygame.display.set_caption("Tic Tac Toe Game By Technical Coderji") # set title of screen
clock = pygame.time.Clock() # initialized clock for time and FPS
FPS = 60 # set FPS

# For Draw window(Anything on window)
def draw_window(win):
    page = stack[-1]

    if page == "homepage":
        draw_home_page(win)
    elif page == "gamepage":
        draw_game_page(win)
    elif page == "vscom":
        draw_com_page(win)
    elif page == "multiplayer":
        draw_multiplayer_page(win)

# For check every event
def check_event(event):
    page = stack[-1]

    if page == "homepage":
        check_event_of_home_page(event)
    elif page == "gamepage":
        check_event_of_game_page(event)
    elif page == "vscom":
        check_event_of_com_page(event)
    elif page == "multiplayer":
        check_event_of_multiplayer_page(event)

def main():
    global stack

    stack.append("homepage")

    #for gameloop
    while True:

        #for event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            check_event(event)

        draw_window(win)

        pygame.display.flip()
        clock.tick(FPS)

if __name__=="__main__":
    main()
    pygame.quit()
    exit()