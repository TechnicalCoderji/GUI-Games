# import usefull modules
import pygame
from load_assets import assets

# a function that initializes all imported Pygame modules
pygame.init()

# Creating window
RES = WIDTH, HEIGHT = 400 ,550 # define width and height
win = pygame.display.set_mode(RES) # make screen/window object
pygame.display.set_caption("Tic TAC TOE Game By Technical Coderji") # set title of screen
clock = pygame.time.Clock() # initialized clock for time and FPS
FPS = 60 # set FPS

fonts = ["Minecraft.ttf",]

#colours
white = (255, 255, 255)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)

#load images
game_assets = {
    "homepage": pygame.transform.scale(pygame.image.load("img\homepage.jpg"),RES),
    "ximage": pygame.transform.scale(pygame.image.load("img/x.png"),(100,100)),
    "oimage": pygame.transform.scale(pygame.image.load("img/o.png"),(100,100)),
    "playbutton":pygame.image.load("img\playbutton.png"),
    "button":pygame.image.load(f"img\\button_rectangle_depth_flat.png")
}

# Functions and Classes
def get_font(font,size):
    return pygame.font.Font(font,size)

def print_text(surface, text, color, x, y, width, height,font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    rect = pygame.Rect(x, y, width, height)
    text_rect.center = rect.center
    # pygame.draw.rect(surface, (0, 0, 0), rect, 2)
    surface.blit(text_surface, text_rect)

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

def game_restart():
    global move_count, game_grids

    move_count = 0
    game_grids = {
    (0,0): None,(0,1): None,(0,2): None,
    (1,0): None,(1,1): None,(1,2): None,
    (2,0): None,(2,1): None,(2,2): None
    }

class GetImage:
    def __init__(self,rect_value,image):
        self.x = rect_value[0]
        self.y = rect_value[1]
        self.image = pygame.transform.scale(image,(rect_value[2:4]))

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))

class ImageButton:
    def __init__(self, x, y, image, width, height, text=None, font=None, font_color=(0, 0, 0)):
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.text = text
        self.font = font
        self.font_color = font_color

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        if self.text and self.font:
            text_surface = self.font.render(self.text, True, self.font_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect.topleft)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# For Draw Homepage
def draw_home_page(win):
    win.fill((51, 153, 218))

    two_play_button.draw(win)
    com_play_button.draw(win)
    online_play_button.draw(win)

# For Draw O
def draw_O(win,x,y,width):
    radius = width//2
    center = (x+radius,y+radius)
    pygame.draw.circle(win,green,center,radius-5,10)

# For Draw X
def draw_X(win,x,y,width):
    pygame.draw.line(win,red,(x+10,y+10),(x+width-10,y+width-10),13)
    pygame.draw.line(win,red,(x+10,y+width-10),(x+width-10,y+10),13)

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

    winner = check_winner()
    if winner:
        output_text = "O WIN THE GAME" if winner == "O" else "X WIN THE GAME" if winner == "X" else "GAME IS TIE"

# For Draw window(Anything on window)
def draw_window(win):
    page = stack[-1]

    if page == "homepage":
        draw_home_page(win)
    elif page == "gamepage":
        draw_game_page(win)

# For check home page event
def check_event_of_home_page(event):
    
    if two_play_button.is_clicked(event):
        stack.append("gamepage")

    elif com_play_button.is_clicked(event):
        print("com")

    elif online_play_button.is_clicked(event):
        print("online")

# For check game page event
def check_event_of_game_page(event):
    global move_count
    
    # For mouse button down check
    if event.type == pygame.MOUSEBUTTONDOWN and check_winner() == None:
        x, y = pygame.mouse.get_pos()
        player = "O" if move_count%2==0 else "X"
        for i,j in game_grids:
            if not game_grids[(i,j)]:
                rect = pygame.rect.Rect(i*120+31,j*120+31,100,100)
                if rect.collidepoint(x,y):
                    game_grids[(i,j)] = player
                    move_count += 1
                    break

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
two_play_button = ImageButton(95, 265, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Player",get_font(fonts[0],25),white)
com_play_button = ImageButton(95, 345, assets["Green"]["button_rectangle_depth_flat"],210,70,"VS Computer",get_font(fonts[0],25),white)
online_play_button = ImageButton(95, 425, assets["Green"]["button_rectangle_depth_flat"],210,70,"Online Play",get_font(fonts[0],25),white)

# IMAGES
clock_bg = GetImage((WIDTH-135,415,120,120),assets["Green"]["button_round_border"])

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