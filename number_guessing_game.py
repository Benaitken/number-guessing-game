import random

print("🎯 Welcome to the Number Guessing Game!") 

while True:
    secret_number = random.randint(1,100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")
    
    while True:
        guess = input("Enter your guess:")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 You got it in {attempts} tries! The number was {secret_number}.")
            break
       
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()          
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break