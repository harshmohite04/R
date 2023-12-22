# Take input from the user for the tuple elements (comma-separated)
try:
    tuple_elements = tuple(map(int, input("Enter the tuple elements (comma-separated): ").split(',')))

    # Take input from the user for K
    k = int(input("Enter the value of K: "))

    # Validate that K is within the range of tuple length
    if not (0 < k <= len(tuple_elements)):
        raise ValueError("Invalid value for K. Should be within the range of tuple length.")

    # Find the maximum and minimum K elements
    max_k_elements = tuple(sorted(tuple_elements, reverse=True)[:k])
    min_k_elements = tuple(sorted(tuple_elements)[:k])

    # Display the results
    print(f"\nMaximum {k} elements: {max_k_elements}")
    print(f"Minimum {k} elements: {min_k_elements}")

except ValueError as e:
    print(f"Invalid input: {e}")
