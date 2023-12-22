class PowerCalculator:
    @staticmethod
    def power(x, n):
        # Base case: x^0 is always 1
        if n == 0:
            return 1

        # Recursive case: x^n = x * x^(n-1)
        if n < 0:
            x = 1 / x
            n = -n

        return x * PowerCalculator.power(x, n - 1)

# Example usage:
try:
    # Take input from the user for base (x) and exponent (n)
    base = float(input("Enter the base (x): "))
    exponent = int(input("Enter the exponent (n): "))

    # Create an instance of the PowerCalculator class
    calculator = PowerCalculator()

    # Call the power method and display the result
    result = calculator.power(base, exponent)
    print(f"{base}^{exponent} = {result}")

except ValueError:
    print("Invalid input. Please enter a valid base (float) and exponent (integer).")
