def count_divisions_by_three(number):
    count = 0

    while number > 10:
        number /= 3
        count += 1

    return count


# Take input from the user for the number
try:
    user_input = float(input("Enter a number: "))

    # Call the function to count divisions by three
    divisions_count = count_divisions_by_three(user_input)

    # Display the result
    print(f"The given number can be divided by 3 {divisions_count} times before it is less than or equal to 10.")

except ValueError:
    print("Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An error occurred: {e}")
