import pygame

pygame.init()

# Creating window
RES = WIDTH, HEIGHT = 490 ,490
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
    "ximage": pygame.transform.scale(pygame.image.load("img/x.png"),(110,110)),
    "oimage": pygame.transform.scale(pygame.image.load("img/o.png"),(110,110))
}

def draw_home_page(win):
    win.blit(game_asserts["homepage"],(0,0))

def draw_game_page(win):
    win.fill((0,0,0))

def draw_window(win):
    page = stack[-1]

    if page == "homepage":
        draw_home_page(win)
    elif page == "gamepage":
        draw_game_page(win)

# Game Related Variable
stack = []

def main():
    global stack

    stack.append("homepage")

    #for gameloop
    while True:

        #for event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stack.append("gamepage")
                if event.key == pygame.K_BACKSPACE:
                    stack.pop()

        draw_window(win)

        pygame.display.flip()
        clock.tick(FPS)

if __name__=="__main__":
    main()
    pygame.quit()
    exit()