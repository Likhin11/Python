import random

def play_game():
    
    print("🎮 NUMBER GUESSING GAME")
    print()
    print("Choose difficulty:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("Enter your choice: ")

    if choice == "1":
        maximum = 50
    elif choice == "2":
        maximum = 100
    elif choice == "3":
        maximum = 200
    else:
        print("Invalid choice!")
        exit()

    number = random.randint(1, maximum)
    attempts = 0

    print()
    print("I have chosen a number between 1 and", maximum)

    while True:
        guess = int(input("Enter your guess: "))

        attempts += 1

        if guess == number:
            print("Correct! 🎉")
            print("You got it in", attempts, "attempts!")
            break
        elif guess > number:
            print("Too high!")
        else:
            print("Too low!")
while True:
    play_game()

    again = input("\nDo you want to play again? (y/n): ")

    if again.lower() != "y":
        print("Thanks for playing! 👋")
        break