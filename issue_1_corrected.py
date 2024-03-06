# Consistent variable naming and comments
def calculate_area(radius, height, side_length, breadth):
    """
    Calculate the total area considering a circle, rectangle, and square.
    
    Parameters:
    - radius (float): Radius of the circle.
    - height (float): Height of the rectangle.
    - side_length (float): Side length of the square.
    - breadth (float): Breadth of the rectangle.

    Returns:
    float: The total area.
    """
    circle_area = 3.14 * radius**2
    rectangle_area = height * breadth  # Area of rectangle
    square_area = side_length**2  # Area of square

    # Complex function with comments
    result = circle_area + rectangle_area - square_area
    return result

# Sample usage
circle_radius = 5
rectangle_height = 10
square_side_length = 4
rectangle_breadth = 6

result = calculate_area(circle_radius, rectangle_height, square_side_length, rectangle_breadth)
print(f"Result: {result}")
