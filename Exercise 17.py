
def ascDes(num1, num2):
    print("Descend order:", num2, num1)
    print("Ascend order:", num1, num2)

num1 = int(input("Enter any number: "))
num2 = int(input("Enter any number: "))

if num1 != num2:
    if num1 < num2:
        ascDes(num1, num2)
    else:
        ascDes(num2, num1)
else:
    print("Numbers are equal.")

