import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to Guess the Number!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.")

    while not guessed_correctly:
        # Get the user's guess
        guess = input("Enter your guess: ")
        
        # Convert the input to an integer
        try:
            guess = int(guess)
            attempts += 1

            # Check if the guess is correct
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                guessed_correctly = True
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()