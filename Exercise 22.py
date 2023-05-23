
def disctSalary(salary):
    if salary <= 1000000:
        percage = .04
    elif salary <= 2000000:
        percage = .07
    else:
        percage = .08

    amount = salary * percage
    netSalary = salary - amount

    return amount, netSalary

salary = float(input("Enter worker salary: "))

disct, netSalary = disctSalary(salary)
print("Discount amount is:", disct)
print("Net salary received by the worker is:", netSalary)
