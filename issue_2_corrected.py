import logging

class ShapeCalculator:
    def __init__(self):
        # Initialize logging
        self.logger = self.setup_logger()

    def calculate_area(self, radius, height, side_length, breadth):
        # Log inputs for debugging
        self.logger.debug(f"Calculating area with inputs: radius={radius}, height={height}, side_length={side_length}, breadth={breadth}")

        circle_area = 3.14 * radius**2
        rectangle_area = height * breadth
        square_area = side_length**2

        result = circle_area + rectangle_area - square_area

        # Log the result for debugging
        self.logger.info(f"Result: {result}")

        return result

    def setup_logger(self):
        # Create a logger
        logger = logging.getLogger("ShapeCalculatorLogger")
        logger.setLevel(logging.DEBUG)

        # Create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Create formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Add formatter to ch
        ch.setFormatter(formatter)

        # Add ch to logger
        logger.addHandler(ch)

        return logger

# Sample usage
calculator = ShapeCalculator()
r = 5
h = 10
s = 4
b = 6

result = calculator.calculate_area(r, h, s, b)
