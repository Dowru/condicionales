
def sumc(num1, num2, num3):
    if num1 + num2 == num3:
        return "Number is equal to the sum of the first and second numbers."
    else:
        return "Number is not equal to the sum of the first and second numbers."

num1 = float(input("Enter any number: "))
num2 = float(input("Enter any number: "))
num3 = float(input("Enter any number: "))

result = sumc(num1, num2, num3)
print(result)
