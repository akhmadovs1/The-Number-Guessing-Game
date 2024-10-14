import random
import art
print(art.logo)

should_continue = True
while should_continue:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    option = str(input("Choose a difficulty. Type 'easy' or 'hard': "))

    random_number = random.randint(1, 100)

    if option == "easy":
        for i in range(1, 11):
            print(f"\nYou have {11 - i} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                print("Oh You found it!")
                break;

    if option == "hard":
        for i in range(1, 6):
            print(f"\nYou have {6 - i} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess < random_number:
                print("Too low!")
            elif guess > random_number:
                print("Too high!")
            else:
                print("Oh You found it!")
                break;
    
    choose_option = str(input("Type 'yes' for continue or 'no' for stop game: "))
    if choose_option == "yes":
        should_continue = True
    else:
        should_continue = False
        print("Game completed successfully!")