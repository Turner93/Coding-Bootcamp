class Rectangle:
    def __init__(self, length, width):
        # Initialize rectangle with length and width
        self.length = length
        self.width = width

    def calculate_area(self):
        # Calculate and return the area of the rectangle
        area = self.length * self.width
        return area

# Sample usage
rectangle_instance = Rectangle(5, 3)
area_of_rectangle = rectangle_instance.calculate_area()
print(f"Area of the rectangle: {area_of_rectangle}")