import pygame

pygame.init()

# Creating window
RES = WIDTH, HEIGHT = 500 ,500
win = pygame.display.set_mode(RES)
pygame.display.set_caption("tictok game by Technical Coderji")
clock = pygame.time.Clock()
FPS = 60

#colour
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)

#load images
game_asserts = {
    "homepage": pygame.transform.scale(pygame.image.load("img\homepage.jpg"),RES),
    "ximage": pygame.transform.scale(pygame.image.load("img/x.png"),(100,100)),
    "oimage": pygame.transform.scale(pygame.image.load("img/o.png"),(100,100)),
    "playbutton":pygame.image.load("img\playbutton.png")
}

# Functions and Classes
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

class ImageButton:
    def __init__(self, x, y, image, width, height):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# For Draw Homepage
def draw_home_page(win):
    win.blit(game_asserts["homepage"],(0,0))
    play_button.draw(win)

# For Draw Main Game Page
def draw_game_page(win):
    win.fill((0,0,0))

    pygame.draw.rect(win,(252, 186, 3),(0,0,*RES),40)

    for i in range(1,3):
        pygame.draw.line(win,(0,255,0),(40,(140*i)+40),(460,(140*i)+40),10)
        pygame.draw.line(win,(0,255,0),((140*i)+40,40),((140*i)+40,460),10)

    for i in game_grids:
        image = None
        if game_grids[i]=="O":
            image = game_asserts["oimage"]
        elif game_grids[i]=="X":
            image = game_asserts["ximage"]

        if image:
            x = (i[0]*140)+60
            y = (i[1]*140)+60
            win.blit(image,(x,y))

# For Draw window(Anything on window)
def draw_window(win):
    page = stack[-1]

    if page == "homepage":
        draw_home_page(win)
    elif page == "gamepage":
        draw_game_page(win)

# For check home page event
def check_event_of_home_page(event):
    
    if play_button.is_clicked(event):
        stack.append("gamepage")

# For check game page event
def check_event_of_game_page(event):
    global move_count
    
    # For mouse button down check
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        player = "O" if move_count%2==0 else "X"
        for i,j in game_grids:
            rect = pygame.rect.Rect(i*140+45,j*140+45,130,130)
            if rect.collidepoint(x,y):
                game_grids[(i,j)] = player
                move_count += 1
                break
            
    print(check_winner())

# For check every event
def check_event(event):
    page = stack[-1]

    if page == "homepage":
        check_event_of_home_page(event)
    elif page == "gamepage":
        check_event_of_game_page(event)

# Game Related Variable
stack = []
game_grids = {
    (0,0): None,(0,1): None,(0,2): None,
    (1,0): None,(1,1): None,(1,2): None,
    (2,0): None,(2,1): None,(2,2): None
}
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

# Objects
play_button = ImageButton(143,328, game_asserts["playbutton"],213,78)

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