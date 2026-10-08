import random


# Prompt player, convert to lowercase, validate, and return choice
def get_player_choice():
    choice = input("Enter rock, paper, scissors: ").lower()

    # Ask until choice is valid
    while choice != "rock" and choice != "paper" and choice != "scissors":
        print(f'Sorry, "{choice}" is not a valid choice. Please try again.')
        choice = input("Enter rock, paper, scissors: ").lower()

    return choice


# Compare the two choices and return "win", "loss", or "tie"
def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "loss"


def main():
    # Welcome the user
    print("Welcome to Rock Paper Scissors!")

    # Ask for the number of rounds and make sure it is an odd number
    rounds_text = input("How many rounds would you like to play: ")
    while not rounds_text.isdigit() or int(rounds_text) % 2 == 0:
        rounds_text = input("Sorry, the number must be an odd number. Please try again: ")
    rounds = int(rounds_text)

    # Variables to keep track of the score and the possible choices
    player_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]

    # Ties don't count -> keep playing until all rounds have a winner
    while player_wins + computer_wins < rounds:
        # Get the player's choice and generate the computer's choice
        player_choice = get_player_choice()
        computer_choice = random.choice(options)
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(player_choice, computer_choice)

        # Update the score or push to the next round if it's a tie
        if result == "win":
            print("You won!")
            player_wins += 1
        elif result == "loss":
            print("You lost!")
            computer_wins += 1
        else:
            print("Tie! Play again.")

    # Print the final score
    print(f"Score — You: {player_wins} | Computer: {computer_wins}")

    # Determine the overall winner
    if player_wins > computer_wins:
        print("You win!!!")
    else:
        print("The computer wins!!!")

    print("Thanks for playing!")


main()