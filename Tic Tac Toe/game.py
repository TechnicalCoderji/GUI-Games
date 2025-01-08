# module for Game Page
import pygame
from core import GetImage,WIDTH,assets,red,green,white,print_text,get_font,fonts,Timer

# variables
game_grids = {(i, j): None for i in range(3) for j in range(3)}
move_count = 0

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
clock_bg = GetImage((WIDTH-135,415,120,120),assets["Green"]["button_round_border"])

# For Draw O
def draw_O(win,x,y,width):
    radius = width//2
    center = (x+radius,y+radius)
    pygame.draw.circle(win,green,center,radius-5,10)

# For Draw X
def draw_X(win,x,y,width):
    pygame.draw.line(win,red,(x+10,y+10),(x+width-10,y+width-10),13)
    pygame.draw.line(win,red,(x+10,y+width-10),(x+width-10,y+10),13)

# For restarting game
def game_restart():
    global move_count, game_grids

    move_count = 0
    game_grids = {
    (0,0): None,(0,1): None,(0,2): None,
    (1,0): None,(1,1): None,(1,2): None,
    (2,0): None,(2,1): None,(2,2): None
    }

# For shifting move
def shift_move():
    global move_count

    move_count += 1
    timer_10_sec.restart()

# timer 10 second
timer_10_sec = Timer(10,WIDTH-75,475,80,80,(252, 211, 3),shift_move)

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

# For check game page event
def check_event_of_game_page(event):
    
    # For mouse button down check
    if event.type == pygame.MOUSEBUTTONDOWN and check_winner() == None:
        x, y = pygame.mouse.get_pos()
        player = "O" if move_count%2==0 else "X"
        for i,j in game_grids:
            if not game_grids[(i,j)]:
                rect = pygame.rect.Rect(i*120+31,j*120+31,100,100)
                if rect.collidepoint(x,y):
                    game_grids[(i,j)] = player
                    shift_move()
                    break

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

    pygame.draw.rect(win,(100,100,100),(0,400,WIDTH,200))
    clock_bg.draw(win)

    timer_10_sec.draw(win)

    winner = check_winner()
    if winner:
        timer_10_sec.running = False
        output_text = "O WIN THE GAME" if winner == "O" else "X WIN THE GAME" if winner == "X" else "GAME IS TIE"
    else:
        timer_10_sec.update()
        text_to_blit = "O's move" if move_count%2==0 else "X's move"
        print_text(win,text_to_blit,white,30,430,200,100,get_font(fonts[0],50))

if __name__ == "__main__":
    pass