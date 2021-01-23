import random
i = 1
while i < 10:
    i = i + 1
    player1 = input("player1 enter a number between 1 and 10:   ")
    player1 = int(player1)
    player2 = random.randint(1, 10)
    print("player2 guess", player2)
    if player1 > player2:
        print("player1 wins")
    elif player2 > player1:
        print("player2 wins")
    else:
        print("Tie")
isExit = input("do you want to exit yes or no:")
if isExit == "yes":
    exit
