import random


def get_choices():
    player_choice = input("Enter the choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(choices):
    player = choices["player"]
    computer = choices["computer"]
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
        return "tie"
    elif player == "rock":
        if computer == "scissors":
            return "lose"
        else:
            return "win"
    elif player == "paper":
        if computer == "rock":
            return "win"
        else:
            return "lose"
    elif player == "scissors":
        if computer == "paper":
            return "win"
        else:
            return "lose"


result = check_win(get_choices())
print(result)
