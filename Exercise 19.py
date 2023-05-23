
def calcuM(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = float(input("Enter any number: "))
num2 = float(input("Enter any number: "))
num3 = float(input("Enter any number: "))

result = calcuM(num1, num2, num3)
print("Mayor number is:", result)
