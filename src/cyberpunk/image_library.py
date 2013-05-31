from constants import *  # @UnusedWildImport

_images = {}
def get_image(filename):
    """Looks in the image directory for filename and loads it.
    Returns pygame.image
    """
    global _images

    if filename not in _images:
        img_path = os.path.join(IMAGE_DIRECTORY, filename + ".png")
        _images[filename] = pygame.image.load(img_path).convert_alpha()

    return _images[filename]
