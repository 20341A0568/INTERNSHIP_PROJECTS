import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Guess the number between 1 and 100!")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")


number_guessing_game()
