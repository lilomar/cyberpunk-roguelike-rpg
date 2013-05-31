import pygame.sprite
import image_library
from constants import *  # @UnusedWildImport

class Sprite(pygame.sprite.DirtySprite):
    def __init__(self, imageName, pos=(0, 0)):
        """ Sets up a sprite, loading an image from Graphics.imageLibrary.
        """
        pygame.sprite.DirtySprite.__init__(self)

        self.fileName = imageName
        self.image = image_library.get_image(imageName)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

class SpriteGroup(pygame.sprite.RenderUpdates):
    def __init__(self, *args, **kwargs):
        pygame.sprite.RenderUpdates.__init__(self, *args, **kwargs)

    def draw(self, surface):
        pygame.sprite.RenderUpdates.draw(self, surface)

    def update(self):
        for sprite in self.sprites():
            sprite.update()
