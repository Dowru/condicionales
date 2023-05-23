
def weeklySalary(hourWork):
    if hourWork <= 20:
        hourRate = 10000
        
    else:
        hourRate = 35000

    salary = hourWork * hourRate
    return salary

hour = float(input("Enter number of hours worked this weakly: "))
salary = weeklySalary(hour)
print(salary)