
import random

def disct(total_purchase):
    rNum = random.randint(1, 100)

    if rNum < 65:
        percge = 0.20
    else:
        percge = 0.30

    amount = purchase * percge
    payment = purchase - amount

    return payment

purchase = float(input("Enter total amount purchase : "))
payment = disct(purchase)
print("Total amount to paid with discount:", payment)
