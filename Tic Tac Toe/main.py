# import usefull modules
import pygame
from core import RES,stack
from game import *
from home import *

# a function that initializes all imported Pygame modules
pygame.init()

# Creating window
win = pygame.display.set_mode(RES) # make screen/window object
pygame.display.set_caption("Tic TAC TOE Game By Technical Coderji") # set title of screen
clock = pygame.time.Clock() # initialized clock for time and FPS
FPS = 60 # set FPS

# For Draw window(Anything on window)
def draw_window(win):
    page = stack[-1]

    if page == "homepage":
        draw_home_page(win)
    elif page == "gamepage":
        draw_game_page(win)

# For check every event
def check_event(event):
    page = stack[-1]

    if page == "homepage":
        check_event_of_home_page(event)
    elif page == "gamepage":
        check_event_of_game_page(event)

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