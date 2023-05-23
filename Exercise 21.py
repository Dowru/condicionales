
def disct(brand):
    if brand == "Honda":
        disctPge = 0.04
    elif brand == "Yamaha":
        disctPge = 0.07
    elif brand == "Suzuki":
        disctPge = 0.15
    else:
        disctPge = 0.03

    return disctPge

brand = input("Enter motorcycle brand: ")

discount = disct(brand)
print("Discount percentage for", brand, "is:", discount * 100, "%")
