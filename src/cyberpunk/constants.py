from __future__ import division  # Changes / to always return a float, use // for integer division

import os

import pygame

# tile size in pixels
TILE_SIZE = 16

# screen starting position and size
SCREEN_RECT = pygame.Rect(0, 0, TILE_SIZE * 20, TILE_SIZE * 20)

# fps and its inverse, both listed so that spf is only calculated once
FRAMES_PER_SECOND = 30
SECONDS_PER_FRAME = 1 / FRAMES_PER_SECOND

# resource directories, relative to src/cyberpunk
IMAGE_DIRECTORY = os.path.join('..', '..', 'img')

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# temp
TILE_IMAGE = os.path.join("tile", "tile")
