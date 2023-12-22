# Pattern 'R'
def print_pattern_R(rows):
    for i in range(rows):
        for j in range(rows):
            if j == 0 or (i == 0 or i == rows - 1) and j < rows - 1 or i == j == rows // 2 or j == rows - 1 and i <= rows // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Pattern 'O'
def print_pattern_O(rows):
    for i in range(rows):
        for j in range(rows):
            if (j == 0 or j == rows - 1) and (i != 0 and i != rows - 1) or (i == 0 or i == rows - 1) and (j > 0 and j < rows - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example: Print patterns with 7 rows
print("Pattern 'R':")
print_pattern_R(7)

print("\nPattern 'O':")
print_pattern_O(7)
