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

def print_text(surface, text, color, x, y,font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x,y)
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

# For Text input class
class TextInputBox:
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = (255, 206, 10)
        self.color_active = (0,0,0)
        self.color = self.color_inactive
        self.text = text
        self.font = font
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.cursor_visible = True  # Toggle cursor visibility
        self.cursor_timer = 0
        self.cursor_interval = 500  # Cursor blinking interval in milliseconds

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if the box is clicked
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Update the box color
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f"Input: {self.text}")
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text surface
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        # Adjust the width if the text is too long
        width = max(self.rect.w, self.txt_surface.get_width()+10)
        self.rect.w = width
        # Update cursor visibility
        self.cursor_timer += pygame.time.get_ticks()
        if self.cursor_timer >= self.cursor_interval:
            self.cursor_visible = not self.cursor_visible
            self.cursor_timer = 0

    def draw(self, screen):
        # Draw the text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Draw the cursor if active
        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + 5 + self.txt_surface.get_width()
            cursor_y_start = self.rect.y + 5
            cursor_y_end = self.rect.y + self.rect.height - 5
            pygame.draw.line(screen, self.color, (cursor_x, cursor_y_start), (cursor_x, cursor_y_end), 2)
        # Draw the input box rect
        pygame.draw.rect(screen, self.color, self.rect, 2)

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