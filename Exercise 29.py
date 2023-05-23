
print("Validate Visual Studio Code shortcuts.")
print("Enter 'yes' if it is correct or 'no' if it is not.")

print("1 | Ctrl+K+C")
print("2 | Ctrl+<")
print("3 | Ctrl+P")

shortcut1 = input("Is shortcut 1 correct? ")
shortcut2 = input("Is shortcut 2 correct? ")
shortcut3 = input("Is shortcut 3 correct? ")

if shortcut1 == 'yes' and shortcut2 == 'no' and shortcut3 == 'yes':
    message = "Congratulations, you're correct!"
else:
    message = "Does not apply."

print(message)

