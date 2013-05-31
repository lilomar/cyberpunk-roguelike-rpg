from __future__ import division  # Changes / to always return a float, use // for integer division

from pygame.constants import *  # @UnusedWildImport

import sprite
import image_library

from constants import *  # @UnusedWildImport

class Charactor(sprite.Sprite):
    def __init__(self, sprite_file_name, pos=(0, 0)):
        # assert self.__class__ != Charactor, 'Use a subclass of ' + self.__class__.__name__

        sprite_file_name = os.path.join('charactor', sprite_file_name)
        sprite.Sprite.__init__(self, sprite_file_name + '_N', pos)
        self._sprite_container = sprite.SpriteGroup([self])

        self._speed = TILE_SIZE
        self._direction = ""

        self._imageN = self.image
        self._imageE = image_library.get_image(sprite_file_name + '_E')
        self._imageS = image_library.get_image(sprite_file_name + '_S')
        self._imageW = image_library.get_image(sprite_file_name + '_W')

        self._image_corpse = image_library.get_image(sprite_file_name + '_corpse')

        self.alive = True

    def process_events(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self._direction = "N"
                elif event.key == K_DOWN:
                    self._direction = "S"
                elif event.key == K_LEFT:
                    self._direction = "W"
                elif event.key == K_RIGHT:
                    self._direction = "E"

    def update(self, level):
        if self.alive:
            # move and update image direction
            if self._direction == "N":
                self.rect.y -= self._speed
                self.image = self._imageN
            elif self._direction == "E":
                self.rect.x += self._speed
                self.image = self._imageE
            elif self._direction == "S":
                self.rect.y += self._speed
                self.image = self._imageS
            elif self._direction == "W":
                self.rect.x -= self._speed
                self.image = self._imageW

            # correct for impassible terrain
            block = level.impassable_rect_check(self.rect)
            if block is not None:
                if self._direction == "N":
                    self.rect.top = block.bottom
                elif self._direction == "E":
                    self.rect.right = block.left
                elif self._direction == "S":
                    self.rect.bottom = block.top
                elif self._direction == "W":
                    self.rect.left = block.right
        self._direction = ""

    def draw(self, screen):
        self._sprite_container.draw(screen)

    def visible_area(self):
        return pygame.Circle()

    def _die(self):
        self.alive = False
        self.image = self._image_corpse
