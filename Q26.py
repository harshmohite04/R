# Take input from the user for the size
try:
    n = int(input("Enter a size: "))

    # Validate that n is a positive integer
    if n <= 0:
        raise ValueError("Size should be a positive integer.")

    # Use a single loop to print lines with stars
    for i in range(1, n + 1):
        print('+' * i)

except ValueError as e:
    print(f"Invalid input: {e}")
