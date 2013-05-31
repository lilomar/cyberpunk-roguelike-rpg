import charactor
import sprite
import item
from constants import *  # @UnusedWildImport

class Scene:
    def __init__(self):
        assert self.__class__ != Scene, 'Use a subclass of ' + self.__class__.__name__

        self.next_scene = self

    def process_events(self, events):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass

class Intro(Scene):
    def __init__(self):
        Scene.__init__(self)

    def process_events(self, events):
        Scene.process_events(self, events)

    def update(self):
        Scene.update(self)

    def draw(self, screen):
        Scene.draw(self, screen)

class Level(Scene):
    def __init__(self):
        Scene.__init__(self)
        self._player = charactor.Charactor("player")
        self._generate_background()

        self._impassible_rects = []
        # level boundaries
        self._impassible_rects.append(pygame.Rect(SCREEN_RECT.left, -TILE_SIZE, SCREEN_RECT.width, TILE_SIZE))
        self._impassible_rects.append(pygame.Rect(SCREEN_RECT.left, SCREEN_RECT.bottom, SCREEN_RECT.width, TILE_SIZE))
        self._impassible_rects.append(pygame.Rect(-TILE_SIZE, SCREEN_RECT.top, TILE_SIZE, SCREEN_RECT.height))
        self._impassible_rects.append(pygame.Rect(SCREEN_RECT.right, SCREEN_RECT.top, TILE_SIZE, SCREEN_RECT.height))

    def _generate_background(self):
        self._background = sprite.SpriteGroup()
        for x in xrange(0, SCREEN_RECT.width, TILE_SIZE):
            for y in xrange(0, SCREEN_RECT.height, TILE_SIZE):
                self._background.add(item.Tile((x, y)))



    def process_events(self, events):
        self._player.process_events(events)

    def update(self):
        self._player.update(self)

    def draw(self, screen):
        self._background.draw(screen)
        self._player.draw(screen)

    def impassable_rect_check(self, rect):
        collision = rect.collidelist(self._impassible_rects)
        if collision != -1:
            return self._impassible_rects[collision]
        else:
            return None


