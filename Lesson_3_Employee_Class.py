

class Employee:

    number_of_employees = 0 # data member for number of employees
    total_salary = 0 # data member for total salary of all employees

    def __init__(self, first, last, salary, department ):   # employee class
        self.first = first
        self.last = last
        self.salary = salary
        self.department = department

        Employee.number_of_employees += 1   # increase number of all employees by one

        Employee.total_salary = Employee.total_salary + salary # increase total salary (PT & FT)

class Full(Employee):   # class Full inherits from Employee class

    Full_salary = 0 # data member for total salary of Full time employees
    Full_number = 0 # data member for number of Full time employees

    def __init__(self, first, last, salary, department):
        Employee.__init__(self, first, last, salary, department)

        Full.Full_number += 1   # increase number of employees (Fulltime)

        Full.Full_salary = Full.Full_salary + salary    # increase total salary (Fulltime)

class Part(Employee): # class Part inherits from Employee class

    Part_salary = 0 # data member for total salary of Part time employees
    Part_number = 0 # data member for number of Part time employees

    def __init__(self, first, last, salary, department):
        Employee.__init__(self, first, last, salary, department)

        Part.Part_number += 1   # increase total salary (Parttime)

        Part.Part_salary = Part.Part_salary + salary    #increase total salary (Parttime)


emp_1 = Full('Young', 'Liu', 98000, "Marketing")
emp_2 = Full('Christine', 'Lang,', 86000, "Nursing")
emp_3 = Full('Rikki', 'Li', 72000, "Pharmacy")
emp_4 = Part('Alvin', 'Chi', 34000, "Security")
emp_5 = Part('Bobby', 'Zhang', 25000, "Technician")


# Average salary functions for all, full and part time employees
Average_Salary_Part = int(Part.Part_salary / Part.Part_number)
Average_Salary_Full = int(Full.Full_salary / Full.Full_number)
Average_Salary_Total = int(Employee.total_salary / Employee.number_of_employees)

print("Total number of employees:", Employee.number_of_employees)
print("Number of Fulltime employees:", Full.Full_number)
print("Number of Parttime employees:", Part.Part_number)

print("Average Salary (Full and Part time): $", Average_Salary_Total)
print("Average Fulltime Salary: $", Average_Salary_Full)
print("Average Parttime Salary: $", Average_Salary_Part)
