from typing import Optional, override
from typing import List
from QuadTreeADT import QuadTreeADT
from Node import Node
from Interval import Interval, Interval2D

class Point:
    def __init__(self, x: object, y: object):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


class QuadTree(QuadTreeADT):
    def __init__(self) -> None:
        self._root: Node = None

    @override
    def clear(self) -> None:
        self._root = None

    @override
    def is_empty(self) -> bool:
        return self._root is None

    @override
    def insert(self, x: object, y: object, value: object) -> None:
        def _insert(current: Node, x: object, y: object, value: object) -> Node:
            if current is None:
                return Node(x, y, value)
            if current.x == x and current.y == y:
                current.value = value
                return current
            elif x < current.x and y >= current.y:
                current.NW = _insert(current.NW, x, y, value)
            elif x < current.x and y < current.y:
                current.SW = _insert(current.SW, x, y, value)
            elif x >= current.x and y >= current.y:
                current.NE = _insert(current.NE, x, y, value)
            elif x >= current.x and y < current.y:
                current.SE = _insert(current.SE, x, y, value)
            return current

        self._root = _insert(self._root, x, y, value)

    @override
    def query_2D(self, rect: Interval2D) -> None:
        def query_2D(current: Node, rect: Interval2D) -> None:
            if current is None:
                return
            x_min = rect.interval_x.min
            x_max = rect.interval_x.max
            y_min = rect.interval_y.min
            y_max = rect.interval_y.max
            if rect.contains(current.x, current.y):
                print(current)
            if x_min < current.x and y_max >= current.y:
                query_2D(current.NW, rect)
            if x_min < current.x and y_min < current.y:
                query_2D(current.SW, rect)
                if x_max >= current.x and y_max >= current.y:
                    query_2D(current.NE, rect)
                if x_max >= current.x and y_min < current.y:
                    query_2D(current.SE, rect)
        query_2D(self._root, rect)

    @override
    def search(self, point: Point) -> object:
        def search(current: Node, x: object, y: object ) -> object:
            if current is None:
                return None
            if current.x == x and current.y == y:
                return current.value
            if x < current.x and y >= current.y:
                return search(current.NW, x, y)
            elif x < current.x and y < current.y:
                return search(current.SW, x, y)
            elif x >= current.x and y >= current.y:
                return search(current.NE, x, y)
            else:
                return search(current.SE, x, y)

        return search(self._root, point.x, point.y)



    @override
    def all_points(self) -> List[Point]:
        pass
