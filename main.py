# TODO: While loop. Make the Rock Paper Scissors
import random

user_has_win = False


def game():
    user = get_choice().lower()
    machine = random.choice(["Rock", "Paper", "Scissors"]).lower()

    print(check_winner(user, machine))


def get_choice():
    answer = input('Choose one "Rock", "Paper", "Scissors"\n')

    return answer


def check_winner(user, machine):
    if user == machine:
        return "tie"
    elif user == "rock" and machine == "scissors" or user == "paper" and machine == "rock" or user == "scissors" and \
            machine == "paper":
        return "user"
    elif user == "rock" and machine == "paper" or user == "scissors" and machine == "paper" or user == "paper" and \
            machine == "scissors":
        return "machine"


while not user_has_win:
    game()
