import random

options = ["rock", "paper", "scissors"]
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Rock beats scissors! You win!")
    elif player == "paper" and computer == "rock":
        print("Paper beats rock! You win!")
    elif player == "scissors" and computer == "paper":
        print("Scissors beats paper! You win!")
    else:
        print("You lose!")
    
    if not input("Play again? (yes/no): ").lower().startswith('y'):
        running = False
    
    print("Thanks for playing!")
    