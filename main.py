# TODO: Print computer choice. Give option to exit when losing
import random

answers = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}


def game():
    user = get_choice()
    machine = answers[random.choice(["rock", "paper", "scissors"])]

    winner = check_winner(user, machine)

    if winner == "user":
        print("Congratulations, you win!")
    elif winner == "machine":
        print("You lost :(")
        answer = input("Do you want to exit? Yes or No\n").lower()
        if answer == "yes":
            exit(0)
        else:
            game()
    elif winner == "tie":
        print("Tie!")
        answer = input("Do you want to exit? Yes or No\n").lower()
        if answer == "yes":
            exit(0)
        else:
            game()


def get_choice():
    answer = input('Choose one "Rock", "Paper", "Scissors"\n').lower()

    if answer == "rock" or answer == "paper" or answer == "scissors":
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
