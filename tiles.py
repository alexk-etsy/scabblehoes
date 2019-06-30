# Definitions of tile point values and count distributions


class Letter:
    point_value = None
    count = None

    def __init__(self, points, count):
        self.point_value = points
        self.count = count

    # allow adding ints or letters together
    # e.g. Tile('a') + 1 or Tile('a') + Tile('a')
    def __add__(self, other):
        if isinstance(other, int):
            return self.point_value + other
        else:
            return self.point_value + other.point_value

    __radd__ = __add__


class Tile:
    letter = None

    def __init__(self, letter_name):
        self.letter = letters[letter_name]

    @property
    def point_value(self):
        return self.letter.point_value

    __add__ = Letter.__add__
    __radd__ = Letter.__add__


letters = {
    "*": Letter(0, 2),
    "a": Letter(1, 9),
    "b": Letter(3, 2),
    "c": Letter(3, 2),
    "d": Letter(2, 4),
    "e": Letter(1, 12),
    "f": Letter(4, 2),
    "g": Letter(2, 3),
    "h": Letter(4, 2),
    "i": Letter(1, 9),
    "j": Letter(8, 1),
    "k": Letter(8, 1),
    "l": Letter(1, 4),
    "m": Letter(3, 2),
    "n": Letter(1, 6),
    "o": Letter(1, 8),
    "p": Letter(3, 2),
    "q": Letter(10, 1),
    "r": Letter(1, 6),
    "s": Letter(1, 4),
    "t": Letter(1, 6),
    "u": Letter(1, 4),
    "v": Letter(4, 2),
    "w": Letter(4, 2),
    "x": Letter(8, 1),
    "y": Letter(4, 2),
    "z": Letter(10, 1),
}
