import pytest
from QuadTree import QuadTree, Point
from Interval import Interval, Interval2D
from typing import Optional
from typing import List
from QuadTreeADT import QuadTreeADT
from Node import Node

@pytest.fixture
def empty_tree():
    return QuadTree()

@pytest.fixture
def sample_tree():
    tree = QuadTree()
    # Insert some sample points
    tree.insert(0, 0, "Origin")
    tree.insert(-1, 1, "NW")
    tree.insert(-1, -1, "SW")
    tree.insert(1, 1, "NE")
    tree.insert(1, -1, "SE")
    return tree

def test_empty_tree(empty_tree):
    assert empty_tree.is_empty() == True

def test_insert_and_search(empty_tree):
    empty_tree.insert(1, 2, "Test Point")
    point = Point(1, 2)
    assert empty_tree.search(point) == "Test Point"

def test_clear(sample_tree):
    sample_tree.clear()
    assert sample_tree.is_empty() == True

def test_search_nonexistent_point(sample_tree):
    point = Point(5, 5)
    assert sample_tree.search(point) is None

def test_query_2D(sample_tree):
    # Create a rectangle that covers the NE and SE quadrants
    interval_x = Interval(0, 2)
    interval_y = Interval(-2, 2)
    rect = Interval2D(interval_x, interval_y)

    # This is a bit tricky to test since query_2D prints rather than returns
    # You might want to modify the implementation to return points instead
    sample_tree.query_2D(rect)  # Will print points in the specified rectangle

def test_multiple_inserts(empty_tree):
    points = [
        (0, 0, "Point1"),
        (1, 1, "Point2"),
        (-1, -1, "Point3"),
        (2, 2, "Point4")
    ]

    for x, y, value in points:
        empty_tree.insert(x, y, value)
        point = Point(x, y)
        assert empty_tree.search(point) == value

def test_boundary_points(empty_tree):
    # Test points at the boundaries
    empty_tree.insert(0, 0, "Center")
    empty_tree.insert(-10, 10, "Far NW")
    empty_tree.insert(10, -10, "Far SE")

    assert empty_tree.search(Point(0, 0)) == "Center"
    assert empty_tree.search(Point(-10, 10)) == "Far NW"
    assert empty_tree.search(Point(10, -10)) == "Far SE"

def test_overwrite_point(empty_tree):
    # Test inserting at the same coordinates
    empty_tree.insert(1, 1, "First")
    empty_tree.insert(1, 1, "Second")
    assert empty_tree.search(Point(1, 1)) == "Second"

def test_query_2D_empty_region(sample_tree):
    # Query an empty region
    empty_region = Interval2D(Interval(10, 20), Interval(10, 20))
    sample_tree.query_2D(empty_region)  # Should not print anything

def test_query_2D_full_region(sample_tree):
    # Query a region that contains all points
    full_region = Interval2D(Interval(-2, 2), Interval(-2, 2))
    sample_tree.query_2D(full_region)  # Should print all points
