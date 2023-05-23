
def discountPrice(price, discountPercentage):
    amount = price * discountPercentage
    price = price - amount
    return price

price = float(input("Enter price of the motorcycle: "))

tuesday = 0.10
saturday = 0.18

priceTuesday = discountPrice(price, tuesday)
priceSaturday = discountPrice(price, saturday)

print("If purchased on Tuesday, price is:", priceTuesday)
print("If purchased on Saturday, price is:", priceSaturday)
