import random


def print_interface():
    print("👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀")
    print("👀      ✊🤚✌️ Rock Paper Scissors            👀")
    print("👀------------------------------------------ 👀")
    print("👀  Options: ✊ rock, 🤚 paper, ✌️ scissor  👀")
    print("👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀👀")


def print_results(player, computer, result):
    print("\nResults:")
    print(f"Player: {player} 🧑")
    print(f"Computer: {computer} 🤖")
    print(result + " 🎉")


def print_score(player_score):
    print(f"\nPlayer Score: {player_score} 🏆")


def main():
    options = ("rock", "paper", "scissor")
    max_score = 0
    player_score = 0

    while True:
        print_interface()
        computer = random.choice(options)
        player = None

        while player not in options:
            player = input("Enter choice (✊ rock, 🤚 paper, ✌️ scissor): ")

        if computer == player:
            result = "It's a tie!"
        elif (player == "paper" and computer == "rock") or \
                (player == "scissor" and computer == "paper") or \
                (player == "rock" and computer == "scissor"):
            result = "You win!"
            player_score += 1
        else:
            result = "You lose!"

        print_results(player, computer, result)
        print_score(player_score)

        user_choice = input("Do you want to play Ragain? (yes/no): ").lower()
        if user_choice != 'yes':
            print(f"\nGame Over. Your final score: {player_score} 🏁")
            break


if __name__ == "__main__":
    main()

    # main funciton means using the funciton direcly when we apply this main program will start direclty
    # not using it as part
