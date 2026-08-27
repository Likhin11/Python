import random


def choose_difficulty():
    print("\n" + "=" * 40)
    print("          CHOOSE DIFFICULTY")
    print("=" * 40)
    print("1. Easy   → 1-50   | 10 attempts")
    print("2. Medium → 1-100  | 8 attempts")
    print("3. Hard   → 1-200  | 6 attempts")

    while True:
        choice = input("\nEnter your choice (1/2/3): ")

        if choice == "1":
            return 50, 10, 10
        elif choice == "2":
            return 100, 8, 20
        elif choice == "3":
            return 200, 6, 30
        else:
            print(" Invalid choice! Please enter 1, 2, or 3.")


def play_game():
    print("\n" + "=" * 40)
    print("        NUMBER GUESSING GAME")
    print("=" * 40)

    maximum, max_attempts, score_multiplier = choose_difficulty()

    number = random.randint(1, maximum)
    attempts = 0

    print(f"\n I have chosen a number between 1 and {maximum}.")
    print(f" You have {max_attempts} attempts.")
    print(" Try to guess the number!\n")

    while attempts < max_attempts:

        try:
            guess = int(input(" Enter your guess: "))

        except ValueError:
            print(" Please enter a valid number!")
            continue

        if guess < 1 or guess > maximum:
            print(f" Enter a number between 1 and {maximum}.")
            continue

        attempts += 1
        remaining = max_attempts - attempts

        if guess == number:
            score = (max_attempts - attempts + 1) * score_multiplier

            print("\n CORRECT!")
            print(f" You found the number: {number}")
            print(f" Attempts used: {attempts}")
            print(f" Your score: {score}")

            return score

        elif guess > number:
            print(" Too high!")

        else:
            print(" Too low!")

        if remaining > 0:
            print(f" Attempts remaining: {remaining}")

    print("\n GAME OVER!")
    print(f"The correct number was: {number}")
    print(" Score: 0")

    return 0


def main():
    total_score = 0
    games_played = 0

    while True:

        score = play_game()

        total_score += score
        games_played += 1

        print("\n" + "=" * 40)
        print("             GAME SUMMARY")
        print("=" * 40)
        print(f"Games played : {games_played}")
        print(f" Total score  : {total_score}")

        again = input("\n Do you want to play again? (y/n): ")

        if again.lower() != "y":
            print("\n" + "=" * 40)
            print("       THANKS FOR PLAYING!")
            print("=" * 40)
            print(f"Games played : {games_played}")
            print(f"Final score  : {total_score}")
            print("Keep practicing and keep coding!")
            break


if __name__ == "__main__":
    main()