player1 = input("player1 enter rock paper or scissors: ")
player2 = input(" player2 enter rock paper or scissors:")
if player1 == "rock" and player2 == "scissors":
    print("player1 wins")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player2 == "rock" and player1 == "scissors":
    print("player2 wins")
elif player2 == "scissors" and player1 == "paper":
    print("player2 wins")
elif player2 == "paper" and player1 == "rock":
    print("player2 wins")
else:
    print("tie")
