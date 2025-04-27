from QuadTree import QuadTree, Point
from Interval import Interval, Interval2D

def main():
    # Create a new QuadTree
    quad_tree = QuadTree()

    print("--- QuadTree Demo ---")

    # Test if tree is empty
    print("\n1. Testing empty tree:")
    print(f"Is tree empty? {quad_tree.is_empty()}")

    # Insert some points
    print("\n2. Inserting points:")
    points_to_insert = [
        (0, 0, "Origin"),
        (1, 1, "Northeast"),
        (-1, 1, "Northwest"),
        (1, -1, "Southeast"),
        (-1, -1, "Southwest"),
        (2, 2, "Far Northeast"),
        (-2, -2, "Far Southwest")
    ]

    for x, y, value in points_to_insert:
        quad_tree.insert(x, y, value)
        print(f"Inserted point ({x}, {y}) with value '{value}'")

    # Search for points
    print("\n3. Searching for points:")
    test_points = [
        Point(0, 0),
        Point(1, 1),
        Point(-1, -1),
        Point(5, 5)  # This point doesn't exist
    ]

    for point in test_points:
        result = quad_tree.search(point)
        if result:
            print(f"Found value '{result}' at point {point}")
        else:
            print(f"No value found at point {point}")

    # Query 2D regions
    print("\n4. Querying regions:")
    print("Points in northeast quadrant (x ≥ 0, y ≥ 0):")
    northeast_region = Interval2D(Interval(0, 3), Interval(0, 3))
    quad_tree.query_2D(northeast_region)

    print("\nPoints in southwest quadrant (x ≤ 0, y ≤ 0):")
    southwest_region = Interval2D(Interval(-3, 0), Interval(-3, 0))
    quad_tree.query_2D(southwest_region)

    # Clear the tree
    print("\n5. Clearing the tree:")
    quad_tree.clear()
    print(f"Is tree empty after clearing? {quad_tree.is_empty()}")

if __name__ == "__main__":
    main()
