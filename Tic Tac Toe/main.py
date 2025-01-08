# import usefull modules
from core import *
from game import *

# a function that initializes all imported Pygame modules
pygame.init()

# Creating window
win = pygame.display.set_mode(RES) # make screen/window object
pygame.display.set_caption("Tic TAC TOE Game By Technical Coderji") # set title of screen
clock = pygame.time.Clock() # initialized clock for time and FPS
FPS = 60 # set FPS

# For restarting game
def game_restart():
    global move_count, game_grids

    move_count = 0
    game_grids = {
    (0,0): None,(0,1): None,(0,2): None,
    (1,0): None,(1,1): None,(1,2): None,
    (2,0): None,(2,1): None,(2,2): None
    }

# For Draw Homepage
def draw_home_page(win):
    win.fill((51, 153, 218))

    two_play_button.draw(win)
    com_play_button.draw(win)
    online_play_button.draw(win)

# For Draw window(Anything on window)
def draw_window(win):
    page = stack[-1]

    if page == "homepage":
        draw_home_page(win)
    elif page == "gamepage":
        draw_game_page(win)

# For check home page event
def check_event_of_home_page(event):
    global timer_10_sec
    
    if two_play_button.is_clicked(event):
        stack.append("gamepage")
        timer_10_sec.restart()

    elif com_play_button.is_clicked(event):
        print("com")

    elif online_play_button.is_clicked(event):
        print("online")

# For check every event
def check_event(event):
    page = stack[-1]

    if page == "homepage":
        check_event_of_home_page(event)
    elif page == "gamepage":
        check_event_of_game_page(event)

# Game Related Variable
stack = []

# Objects
two_play_button = ImageButton(95, 265, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Player",get_font(fonts[0],25),white)
com_play_button = ImageButton(95, 345, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Computer",get_font(fonts[0],25),white)
online_play_button = ImageButton(95, 425, assets["Green"]["button_rectangle_depth_flat"],210,70,"Online Play",get_font(fonts[0],25),white)

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