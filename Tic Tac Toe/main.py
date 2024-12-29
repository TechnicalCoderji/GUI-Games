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
    "ximage": pygame.image.load("img/x.png"),
    "oimage": pygame.image.load("img/o.png"),
    "playbutton":pygame.image.load("img\playbutton.png")
}

# Functions and Classes
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
    pass

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