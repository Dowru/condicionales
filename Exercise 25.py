def guess_character():
    print("Guess the Marvel character!")
    print("Answer the following questions with 'y' for yes or 'n' for no.")

    can_fly = input("Can it fly? ")
    is_human = input("Is it human? ")
    has_mask = input("Does it wear a mask? ")

    if can_fly == 'yes' and is_human == 'no' and has_mask == 'yes':
        character = "Iron Man"
    elif can_fly == 'no' and is_human == 'yes' and has_mask == 'no':
        character = "Spider-Man"
    elif can_fly == 'yes' and is_human == 'no' and has_mask == 'no':
        character = "Thor"
    else:
        character = "The character couldn't be determined"

    print("The Marvel character is:", character)

guess_character()
