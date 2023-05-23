
def pPT(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 win!"
    else:
        return "Player 2 win!"

player1_choice = input("Enter the choice of Player 1 (rock, paper, scissors): ")
player2_choice = input("Enter the choice of Player 2 (rock, paper, scissors): ")

result = pPT(player1_choice, player2_choice)
print(result)
