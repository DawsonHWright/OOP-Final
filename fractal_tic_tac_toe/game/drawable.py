from pygame import Surface


class Drawable:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREY = (180, 180, 180)
    GREEN = (0, 255, 0)
    DARK_GREY = (100, 100, 100)

    def draw(self, surface: Surface, margin: float) -> None:
        raise NotImplementedError("Subclasses must implement draw method")
