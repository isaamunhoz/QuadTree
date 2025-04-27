
class Node:
    def __init__(self, x: object, y: object, value: object) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.NW, self.NE, self.SE, self.SW = None, None, None, None
    def __str__(self) -> str:
        return "({}, {}) {}".format(self.x, self.y, self.value)
