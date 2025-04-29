from drawable import Drawable
from pygame import Surface
from pygame import draw
from pygame import Rect


class Square(Drawable):
    def __init__(self):
        self.status = -1

    def isOwned(self) -> bool:
        return self.status != -1

    def playHere(self, player: int) -> bool:
        if self.status == -1:
            self.status = player
            return True
        else:
            return False

    def draw(self, surface, margin: float, play_mode: int = 0, playable: (int, int) = None):
        size_x, size_y = surface.get_size()
        my_margin = round(size_x * margin)
        my_rect = surface.get_rect().inflate(-my_margin * 2, -my_margin * 2)

        """
        if play_mode == -1 and self.status == -1:
            draw.rect(surface, Drawable.DARK_GREY, surface.get_rect())
        """

        if self.status == 0:
            center = my_rect.center
            radius = min(my_rect.width, my_rect.height) // 2 - my_margin
            draw.circle(surface, Drawable.BLUE, center, radius, my_margin)
        elif self.status == 1:
            draw.line(surface, Drawable.RED, my_rect.topleft, my_rect.bottomright, my_margin)
            draw.line(surface, Drawable.RED, my_rect.topright, my_rect.bottomleft, my_margin)