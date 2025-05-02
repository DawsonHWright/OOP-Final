from pygame import Surface
from pygame import Rect
from pygame import draw
from typing import Any
from drawable import Drawable
from square import Square


class Board(Drawable):
    _children: list[list[Drawable]]
    _status: int

    def __init__(self, isBig: bool) -> None:
        if isBig:
            self._children =\
                [[Board(False) for _ in range(3)] for _ in range(3)]
        else:
            self._children =\
                [[Square() for _ in range(3)] for _ in range(3)]
        self.status = -1
        self.isBig = isBig

    def isWon(self) -> int:
        def get_status(obj: Any) -> int:
            return obj.status if obj else -1

        for i in range(3):
            # Rows
            if all(get_status(self._children[i][j]) ==
                   get_status(self._children[i][0]) != -1 for j in range(3)):
                return get_status(self._children[i][0])
            # Columns
            if all(get_status(self._children[j][i]) ==
                   get_status(self._children[0][i]) != -1 for j in range(3)):
                return get_status(self._children[0][i])

        # Diagonals
        if all(get_status(self._children[i][i]) ==
               get_status(self._children[0][0]) != -1 for i in range(3)):
            return get_status(self._children[0][0])
        if all(get_status(self._children[i][2-i]) ==
               get_status(self._children[0][2]) != -1 for i in range(3)):
            return get_status(self._children[0][2])

        # Stalemate
        if all(get_status(self._children[i][j]) != -1
               for i in range(3) for j in range(3)):
            self.status = 2
            return 2  # Draw
        return -1

    def draw(self, surface: Surface, margin: float, play_mode: int = 0,
             playable: (int, int) = None) -> None:
        size_x, size_y = surface.get_size()
        my_margin = int(margin * size_x)

        # Working area, leaving margin on the outside
        working_rect = surface.get_rect().inflate(-2 * my_margin,
                                                  -2 * my_margin)
        cell_w = (working_rect.width - 2 * my_margin) / 3
        cell_h = (working_rect.height - 2 * my_margin) / 3

        if play_mode == -1 or self.status == 2:
            draw.rect(surface, Drawable.DARK_GREY, surface.get_rect())

        # Draw children first
        for row in range(3):
            for col in range(3):
                x = working_rect.left + col * (cell_w + my_margin)
                y = working_rect.top + row * (cell_h + my_margin)
                w = cell_w
                h = cell_h
                sub = surface.subsurface(Rect(x, y, w, h))
                if playable is not None and (row, col) != playable:
                    self._children[row][col].draw(sub, margin, play_mode=-1)
                else:
                    self._children[row][col].draw(sub, margin)

        # Draw grid lines last, OVER everything
        for i in range(1, 3):
            # Horizontal lines
            y = working_rect.top + i * (cell_h + my_margin) - my_margin // 2
            draw.line(surface, Drawable.WHITE,
                      (working_rect.left, y),
                      (working_rect.right, y),
                      my_margin)

            # Vertical lines
            x = working_rect.left + i * (cell_w + my_margin) - my_margin // 2
            draw.line(surface, Drawable.WHITE,
                      (x, working_rect.top),
                      (x, working_rect.bottom),
                      my_margin)
