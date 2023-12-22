from datetime import datetime

def calculate_days_between_dates(date1, date2):
    # Convert the date strings to datetime objects
    date_format = "%Y-%m-%d"
    datetime1 = datetime.strptime(date1, date_format)
    datetime2 = datetime.strptime(date2, date_format)

    # Calculate the difference in days
    delta = abs(datetime2 - datetime1)
    return delta.days

# Take input from the user for the two dates
try:
    date_str1 = input("Enter the first date (YYYY-MM-DD): ")
    date_str2 = input("Enter the second date (YYYY-MM-DD): ")

    # Call the function to calculate the number of days
    days_difference = calculate_days_between_dates(date_str1, date_str2)

    # Display the result
    print(f"Number of days between {date_str1} and {date_str2}: {days_difference} days")

except ValueError as e:
    print(f"Error: {e}. Please enter dates in the format YYYY-MM-DD.")
except Exception as e:
    print(f"An error occurred: {e}")

