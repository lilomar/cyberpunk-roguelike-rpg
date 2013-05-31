import time

from pygame.locals import *  # @UnusedWildImport

import scene
from constants import *  # @UnusedWildImport

class Engine:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        pygame.display.set_caption('Working Title')
        # pygame.mouse.set_visible(0)

        self.current_scene = scene.Level()
        self.previous_scene = None

        self._delay = time.clock()

    def run(self):
        """Main game loop. Runs continuously.
        """
        finished = False

        while not finished:

            # Process Events
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    finished = True

            self.current_scene.process_events(events)

            # Update
            self.current_scene.update()

            # Redraw
            self.current_scene.draw(self.screen)

            # Update time and delay
            new_time = time.clock()
            sleep_time = SECONDS_PER_FRAME - (new_time - self._delay)
            if sleep_time > 0:
                time.sleep(sleep_time)
            pygame.display.flip()
            self._delay = new_time

            # Go to next Scene
            if finished:
                self.previous_scene = self.current_scene
                self.current_scene = None

            elif self.current_scene != self.current_scene.next_scene:
                self.previous_scene = self.current_scene
                self.current_scene = self.current_scene.next_scene

        pygame.quit()

if __name__ == "__main__":
    e = Engine()
    e.run()
