
hourWork = float(input("Enter number of hours work: "))
hourRate = float(input("Enter hour rate: "))
category = input("Enter the employee category (A, B, C, D): ")

if category == 'A':
    percentage = 0.10
elif category == 'B':
    percentage = 0.15
elif category == 'C':
    percentage = 0.23
elif category == 'D':
    percentage = 0.25
else:
    print("Invalid category. Please enter a valid category (A, B, C, D).")
    percentage = 0

if percentage > 0:
    baseSalary = hourWork * hourRate
    amount = baseSalary * percentage
    totalSalary = baseSalary + amount

    print("Base Salary:", baseSalary)
    print("Increment Amount:", amount)
    print("Total Salary:", totalSalary)
