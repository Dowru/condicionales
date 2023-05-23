
num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")

elif num1 % 2 == 0 or num2 % 2 == 0:
    print("One of the numbers is even.")
else:
    print("Neither of the numbers is even.")
