
name = input("Enter your Name: ")
finalNote = float(input("Enter your Final Note from 0 to 5: "))
semesterClasses = int(input("Enter number of Semester Classes: "))
numberOfFailures = int(input("Enter number of failures: "))
notes = "You did not pass your fourth grade and it has a value of 0"

if numberOfFailures >= semesterClasses*.30:
    print(notes)
elif finalNote <= 3.5:
    print(notes)
else:
    print(f"{name}, you got a grade of {finalNote}, you are an amazing student, keep it up.")