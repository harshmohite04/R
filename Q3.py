def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Assume the current index is the minimum
        min_index = i

        # Check the rest of the elements to find the minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_list = [64, 25, 12, 22, 11]

print("Original list:", my_list)

# Sort the list using selection sort
selection_sort(my_list)

print("Sorted list:", my_list)