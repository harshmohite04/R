class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example usage:
# Create a rectangle with length 5 and width 3
my_rectangle = Rectangle(5, 3)

# Compute and print the area of the rectangle
area = my_rectangle.compute_area()
print(f"The area of the rectangle is: {area}")
