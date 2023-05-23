
gender = input("Enter the gender ('M' for male, 'F' for female): ")
height = float(input("Enter the height in meters: "))
age = int(input("Enter the age: "))
status = input("Enter the marital status ('S' for single, 'M' for married): ")

if gender == 'F':
    if height > 1.60 and 20 <= age <= 25 and status == 'S':
        print("The female applicant is eligible to join the army.")
    else:
        print("The female applicant is not eligible to join the army.")
elif gender == 'M':
    if height > 1.65 and 18 <= age <= 24 and status == 'S':
        print("The male applicant is eligible to join the army.")
    else:
        print("The male applicant is not eligible to join the army.")
else:
    print("Invalid gender. Please enter a valid gender (M for male, F for female).")
