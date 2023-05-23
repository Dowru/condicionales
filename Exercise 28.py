
def aDisct(price, percentage):
    amount = price * percentage
    price = price - amount
    return price

value = float(input("Enter the purchase value: "))

if value > 40000:
    color = input("Enter the color of the ball (red, white, black, yellow, green): ")

    if color == 'red':
        percentage = 0.10
    elif color == 'white':
        percentage = 0.15
    elif color == 'black' or color == 'yellow':
        percentage = 0.20
    elif color == 'green':
        percentage = 0.30
    else:
        print("Invalid color. No discount will be applied.")
        percentage = 0

    if percentage > 0:
        disct = value * percentage
        netPce = aDisct(value, percentage)

        print("Discount:", disct)
        print("Net price to pay:", netPce)
    else:
        print("No discount will be applied.")
else:
    print("No discount will be applied. Purchase value is less than or equal to 40000.")
