# TODO: While loop. Make the Rock Paper Scissors
import random


def game():
    user = get_choice()
    machine = random.choice(["Rock", "Paper", "Scissors"])

    print(f"User: {user}. Me: {machine}")


def get_choice():
    answer = input('Choose one "Rock", "Paper", "Scissors"\n')

    return answer


def check_winner(user, machine):
    if user == machine:
        return "Tie"
    elif user == "Rock" and machine == "Paper":
        return "User wins!"


game()
