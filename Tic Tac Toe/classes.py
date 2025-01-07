import pygame
import math

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
        self.running = True

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