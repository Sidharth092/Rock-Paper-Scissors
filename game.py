from random import randint

choice = ["rock", "paper", "scissors"]

Bot = choice[randint(0,2)]

player = False

while player == False:
    print("Best of luck")
    player = input("rock, paper, scissors?")
    if player == Bot:
        print("Tie!\n")

    elif player == "rock":
        if Bot == "paper":
            print("You Lose!\n", Bot, "covers", player, "\nBetter luck next time\n") 
        else:
            print("You WIN!\n", player, "smashes", Bot,"\n")

    elif player == "paper":
        if Bot == "scissors":
            print("You Lose!\n", Bot, "cut", player,"\nBetter luck next time\n")
        else:
            print("You WIN!\n", player, "covers", Bot,"\n") 

    elif player == "scissors":
        if Bot == "rock":
            print("You Lose!\n", Bot, "smashes", player,"\nBetter luck next time\n")
        else:
            print("You WIN!\n", player, "cuts", Bot,"\n")

    else:
        print("Not valid. Check your spelling!")

    player = False
    Bot = choice[randint(0,2)]
      