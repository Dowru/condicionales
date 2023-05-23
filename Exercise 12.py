
def mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))
result = mayor(num1, num2)
print("The more number is:", result)
