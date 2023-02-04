from random import choice as rnd


while True:
    Player_Action = input("Enter a choice rock / paper / scissors : ")
    Actions = ["paper", "scissors", "rock"]
    Computer_Action = rnd(Actions)

    if Player_Action == "rock":
        if Computer_Action == "rock":
            print("equal")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

        elif Computer_Action == "paper":
            print ("Computer is Win")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

        elif Computer_Action == "scissors":
            print("Player is Win")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

    #---------------------------------------------------------------------------------------------------

    if Player_Action == "paper":
        if Computer_Action == "paper":
            print("equal")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

        elif Computer_Action == "scissors":
            print ("Computer is Win")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

        elif Computer_Action == "rock":
            print("Player is Win")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

    #---------------------------------------------------------------------------------------------------

    if Player_Action == "scissors":
        if Computer_Action == "scissors":
            print("equal")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

        elif Computer_Action == "rock":
            print ("Computer is Win")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

        elif Computer_Action == "paper":
            print("Player is Win")
            print(f"\nPlayer chose {Player_Action}, Computer chose {Computer_Action}.\n")

    play_again = input("Play again? (yes Or no): ")
    if play_again.lower() != "yes":
        break