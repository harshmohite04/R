# Function to calculate factorial
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial

# Function to reverse the digits of a number
def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

# Take input from the user for the number
try:
    user_number = int(input("Enter a number: "))

    # Check if the number is non-negative
    if user_number < 0:
        print("Please enter a non-negative integer.")
    else:
        # Calculate factorial of the number
        factorial_result = calculate_factorial(user_number)

        # Reverse the digits of the number
        reversed_result = reverse_number(user_number)

        # Display the results
        print(f"\nFactorial of {user_number}: {factorial_result}")
        print(f"Reverse of {user_number}: {reversed_result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
