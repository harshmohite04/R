def create_third_list(list1, list2):
    third_list = list1[1::2] + list2[0::2]
    return third_list

# Example:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result_list = create_third_list(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("Third List:", result_list)
