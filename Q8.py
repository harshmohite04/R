def print_pattern_O(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("***")
        else:
            print("*  *")

# Example: Print the 'O' pattern with 7 rows
print("Pattern 'O':")
print_pattern_O(7)


def print_pattern_P(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("****")
        else:
            print("*")
            if rows // 2 == i:
                print("*")
            else:
                print("*")

# Example: Print the 'P' pattern with 7 rows
print("\nPattern 'P':")
print_pattern_P(7)

