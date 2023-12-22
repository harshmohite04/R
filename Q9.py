class Employee:
    total_employees = 0
    male_count = 0
    female_count = 0

    def __init__(self, name, designation, gender, join_date, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.join_date = join_date
        self.salary = salary

        # Update counts when a new employee is created
        Employee.total_employees += 1
        if gender.lower() == 'male':
            Employee.male_count += 1
        elif gender.lower() == 'female':
            Employee.female_count += 1

    @staticmethod
    def total_employee_count():
        return Employee.total_employees

    @staticmethod
    def count_male_female():
        return Employee.male_count, Employee.female_count

    def salary_above_10000(self):
        return self.salary > 10000

    def is_manager(self):
        return self.designation.lower() == 'manager'


# Example Usage:
employee1 = Employee("John Doe", "Manager", "Male", "2022-01-01", 15000)
employee2 = Employee("Jane Smith", "Developer", "Female", "2022-02-01", 12000)
employee3 = Employee("Bob Johnson", "Manager", "Male", "2022-03-01", 11000)

# Total number of employees
print("Total Employees:", Employee.total_employee_count())

# Count of male and female employees
male_count, female_count = Employee.count_male_female()
print("Male Employees:", male_count)
print("Female Employees:", female_count)

# Employees with salary above 10,000
high_salary_employees = [employee for employee in [employee1, employee2, employee3] if employee.salary_above_10000()]
print("Employees with Salary above 10,000:", [employee.name for employee in high_salary_employees])

# Employees with designation "Manager"
manager_employees = [employee for employee in [employee1, employee2, employee3] if employee.is_manager()]
print("Employees with Designation 'Manager':", [employee.name for employee in manager_employees])
