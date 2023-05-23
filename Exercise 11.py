def evenOdd(number):
    if number % 2 == 0:
        return "This number is even"
    else:
        return "This number is odd"


number = int(input("Enter any number: "))
result = evenOdd(number)
print(result)
