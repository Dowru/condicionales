
name = input("Insert your name: ")
registrationValue = float(input("Insert tuition value: "))
asking = input("Are you a graduate of the university?: ")
otherDiscount = registrationValue * 0.3
discount = registrationValue - otherDiscount

if asking == "YES" or asking == "yes":
    print(f"\n\nName {name}\nValue Registration: {discount}")

else:
    print(f"\n\nName {name}\nValue Registration: {registrationValue}")