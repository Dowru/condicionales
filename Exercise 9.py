
name = input("Enter your firts name: ")
note1 = input("Enter you first note: ")
note2 = input("Enter you second note: ")
note3 = input("Enter you third note: ")
finalNote = note1+note2+note3//3

if finalNote >=10:
    print(f"{name} You passed")
else:
    print(f"{name} Did not pass")