import random

def guess_number():
    
    secret_number = random.randint(1, 100)
    
    
    attempts = 0
    guessed = False
    
    print("Welcome to the Guess the Number game!")
    
    while not guessed:
        try:
            
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1
            
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts to win the game.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


guess_number()
