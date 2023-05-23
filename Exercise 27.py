
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choice (1-4): ")

num1 = float(input("Enter any number: "))
num2 = float(input("Enter any number: "))

if choice == '1':
    result = add(num1, num2)
    print("Result of addition is:", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result of subtraction is:", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result of multiplication is:", result)
elif choice == '4':
    result = divide(num1, num2)
    print("Result of division is:", result)
else:
    print("Invalid choice. Please select option (1-4).")
