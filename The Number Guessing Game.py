import random
import art

print(art.logo)  

def play_game(attempts):
    random_number = random.randint(1, 100)
    
    for i in range(attempts):
        print(f"\nYou have {attempts - i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print(f"Congratulations! You found the number {random_number}!")
            return  
            
    print(f"You've run out of guesses. The number was {random_number}. You lose!")

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    option = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if option == "easy":
        play_game(attempts=10)
    elif option == "hard":
        play_game(attempts=5)
    else:
        print("Invalid option! Please choose 'easy' or 'hard'.")

should_continue = True
while should_continue:
    start_game()
    choose_option = input("Type 'yes' to continue or 'no' to stop the game: ").lower()
    
    if choose_option == "no":
        should_continue = False
        print("Game completed successfully!")
