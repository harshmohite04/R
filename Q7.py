def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end="   ")
        print()

# Example: Print a number pyramid with 3 rows
print("Number Pyramid Pattern:")
print_number_pyramid(3)
