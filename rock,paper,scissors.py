import random
play=True
while play:
    choices = ["rock", "paper", "scissors"]
    computer=random.choice(choices)
    player = None
    def printchoice():
        print("Player: "+ player)
        print("Computer: "+ computer)
    while player  not in choices:
        player = input("Enter your choice?(rock,paper or scissors): ").lower()

    if player == computer:
        printchoice()
        print("Tie!")

    elif player == "rock":
        printchoice()
        print("You win!") if computer == "scissors" else print("You lose!")
    elif player == "paper":
        printchoice()
        print("You win!") if computer == "rock" else print("You lose!")

    elif player == "scissors":
        printchoice()
        print("You win!") if computer == "paper" else print("You lose!")
    
    play_again = None
    while play_again!= "yes" and play_again!= "no":
        play_again = input("Do you want to play again?(yes or no): ").lower()
        
    if play_again == "no":
        break
    elif play_again == "yes":
        continue
    else:
        print("Please enter yes or no")