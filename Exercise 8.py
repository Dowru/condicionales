
print("Check income status.")
print("Answer the following questions with 'yes'  or 'no' ")

hasCash = input("Do you have cash? ")
cashAmount = float(input("Enter the cash amount: "))

if hasCash == 'no':
    status = "You are in the red."
elif cashAmount < 2000:
    status = "You should strive to work more."
elif cashAmount < 3000:
    status = "You are doing reasonably well."
else:
    status = "You have a good financial status."

print("Income Status:", status)