import os
import pygame

directory = 'UI pack'
assets = {}

# Walk through all subdirectories and files in the given directory
for root, subdirs, files in os.walk(directory):
    for subdir in subdirs:
        assets[subdir] = {}
    
    for file in files:
        if file.endswith('.png'):
            path = os.path.join(root, file)
            image = pygame.image.load(path)
            # Extract subdir name and file name without extension
            subdir = os.path.basename(os.path.dirname(path))
            name = os.path.splitext(os.path.basename(file))[0]
            if subdir in assets:
                assets[subdir][name] = image
            else:
                assets[subdir] = {name: image}