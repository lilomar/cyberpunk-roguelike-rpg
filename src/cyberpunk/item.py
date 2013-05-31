
import sprite
from constants import *  # @UnusedWildImport

class Item(sprite.Sprite):
    def __init__(self, sprite_file_name, position=(0, 0)):
        assert self.__class__ != Item, 'Use a subclass of ' + self.__class__.__name__

        sprite.Sprite.__init__(self, os.path.join('items', sprite_file_name), position)

        self.passable = True

    def update(self):
        sprite.Sprite.update(self)

    def collision(self, player):
        """React to a collision with the player.
        """
        pass

class Tile(Item):
    def __init__(self, position):
        Item.__init__(self, TILE_IMAGE, position)
