# Function to calculate gross salary
def calculate_gross_salary(basic_pay):
    hra = 0.10 * basic_pay
    ta = 0.05 * basic_pay
    gross_salary = basic_pay + hra + ta
    return gross_salary


# Function to calculate net salary after deductions
def calculate_net_salary(gross_salary):
    professional_tax = 0.02 * gross_salary
    net_salary = gross_salary - professional_tax
    return net_salary


# Take input from the user for basic pay
try:
    basic_pay = float(input("Enter the basic pay of the employee: "))

    # Check if basic pay is non-negative
    if basic_pay < 0:
        print("Basic pay should be a non-negative value.")
    else:
        # Calculate gross salary
        gross_salary = calculate_gross_salary(basic_pay)

        # Calculate net salary after deductions
        net_salary = calculate_net_salary(gross_salary)

        # Display the results
        print(f"\nGross Salary: {gross_salary:.2f}")
        print(f"Net Salary (after deductions): {net_salary:.2f}")

except ValueError:
    print("Invalid input. Please enter a numerical value for basic pay.")
