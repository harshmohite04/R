def print_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="   ")
        print()

# Example: Print a pyramid with 3 rows
print("Pyramid Pattern:")
print_pyramid(3)

def print_rectangular_pattern(rows, columns):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            print("*", end="   ")
        print()

# Example: Print a rectangular pattern with 3 rows and 3 columns
print("\nRectangular Pattern:")
print_rectangular_pattern(3, 3)
