# TODO: While loop. Make the Rock Paper Scissors
import random

answers = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}


def game():
    user = get_choice()
    machine = answers[random.choice(["Rock", "Paper", "Scissors"])]

    winner = check_winner(user, machine)

    if winner == "user":
        print("Congratulations, you win!")
    elif winner == "machine":
        print("You lost :(")
        game()
    elif winner == "tie":
        print("Tie!")
        game()


def get_choice():
    answer = input('Choose one "Rock", "Paper", "Scissors"\n')

    if answer == "Rock" or answer == "Paper" or answer == "Scissors":
        answer = answers[answer]
    else:
        answer = get_choice()
    return answer


def check_winner(user, machine):
    if user == machine:
        return "tie"
    elif user == 1 and machine == 2 or user == 3 and machine == 1 or user == 2 and \
            machine == 3:
        return "user"
    elif user == 1 and machine == 3 or user == 3 and machine == 2 or user == 2 and \
            machine == 1:
        return "machine"


game()
