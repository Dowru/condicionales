
def low(num1, num2, num3):
    lower = num1

    if num2 < lower:
        lower = num2

    elif num3 < lower:
        lower = num3

    return lower

num1 = float(input("Enter any number: "))
num2 = float(input("Enter any number: "))
num3 = float(input("Enter any number: "))

result = low(num1, num2, num3)
print("The smallest number is:", result)
