
def payment(quantity, priceShirt):
    cost = quantity * priceShirt

    if quantity >= 3:
        discount = .15
    else:
        discount = .05

    amount = cost * discount
    totalPayment = cost - amount

    return totalPayment

quantity = int(input("Enter the quantity of shirts: "))
price = float(input("Enter the price for shirt: "))

totalPayment = payment(quantity, price)
print("Total amount to paid :", totalPayment)
