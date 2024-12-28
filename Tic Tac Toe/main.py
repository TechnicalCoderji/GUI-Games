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

def draw_window(win):
    draw_home_page(win)

def main():

    #for gameloop
    while True:

        #for event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        draw_window(win)

        pygame.display.flip()
        clock.tick(FPS)

if __name__=="__main__":
    main()
    pygame.quit()
    exit()