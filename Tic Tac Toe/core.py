import pygame
import math
from load_assets import assets

pygame.init()

# Variables

# Game Related Variable
stack = []

# colors
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)

# define width and height
RES = WIDTH, HEIGHT = 400 ,550

# List of fonts
fonts = ["Minecraft.ttf",]

#load images
game_assets = {
    "homepage": pygame.transform.scale(pygame.image.load("img\homepage.jpg"),RES),
    "ximage": pygame.transform.scale(pygame.image.load("img/x.png"),(100,100)),
    "oimage": pygame.transform.scale(pygame.image.load("img/o.png"),(100,100)),
    "playbutton":pygame.image.load("img\playbutton.png"),
    "button":pygame.image.load(f"img\\button_rectangle_depth_flat.png")
}

# Functions

# Return Font of desire size
def get_font(font,size):
    return pygame.font.Font(font,size)

def print_text(surface, text, color, x, y, width, height,font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    rect = pygame.Rect(x, y, width, height)
    text_rect.center = rect.center
    # pygame.draw.rect(surface, (0, 0, 0), rect, 2)
    surface.blit(text_surface, text_rect)

# Classes

# For set timer
class Timer:
    def __init__(self, duration, x, y, width, height, color, callback):
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.callback = callback
        self.running = False

    def restart(self):
        self.start_time = pygame.time.get_ticks()
        self.running = True

    def update(self):
        if not self.running:
            return
        
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        if elapsed_time >= self.duration:
            self.running = False
            self.callback()
    
    def draw(self, screen):
        if not self.running:
            elapsed_time = 0
        else:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

        fraction = min(elapsed_time / self.duration, 1)
        
        # Draw the pie slice
        start_angle = -90
        end_angle = start_angle + (fraction * 360)
        points = [(self.x, self.y)]
        
        if fraction > 0:
            for angle in range(int(start_angle), int(end_angle)):
                rad = math.radians(angle)
                x = self.x + (self.width // 2) * math.cos(rad)
                y = self.y + (self.height // 2) * math.sin(rad)
                points.append((x, y))
            
            points.append((self.x, self.y))
            pygame.draw.polygon(screen, self.color, points)

# For get image
class GetImage:
    def __init__(self,rect_value,image):
        self.x = rect_value[0]
        self.y = rect_value[1]
        self.image = pygame.transform.scale(image,(rect_value[2:4]))

    def draw(self,screen):
        screen.blit(self.image,(self.x,self.y))

# Image as well as functinalitys of button
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
    
if __name__ == "__main__":
    pass