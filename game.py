import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\n")


levels = {
        1: 'Easy',
        2: 'Medium',
        3: 'Hard'
    }

def play_game():
    computerChoice = random.randint(1,100)

    for i in range(1, numberOfChances+1):
        try:
            userChoice = int(input('guess the number from 1-100: '))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if not 1 <= userChoice <= 100:
            print("Out of range! Please guess between 1 and 100.\n")
            continue

        if userChoice > computerChoice:
            print('Too high!\n')
        elif userChoice < computerChoice:
            print('Too low!\n')
        else:
            print('Wooow! Congrats!!! You guessed it! 🎉')
            print(f'You guessed it in {i} chance(s)\n')
            return


    print('Out of chances... Failed! The correct number was:', computerChoice)


def get_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ['y', 'n']:
            return ans
        print("Enter valid input (y/n)")

while True:

    print('Please select the difficulty level:\n 1. Easy (10 chances)\n 2. Medium (5 chances)\n 3. Hard (3 chances)\n')

    try:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            numberOfChances = 10
        elif choice == 2:
            numberOfChances = 5
        elif choice == 3:
            numberOfChances = 3
        else:
            print('Please choose a valid option from the menu.\n')
            continue
    except ValueError:
        print('Please enter a valid number.\n')
        continue

    print(f"Congratulations! You have chosen the {levels[choice]} level with {numberOfChances} chances.\nLet's start the game!\n")

    play_game()

    again = get_yes_no("Do you want to play again? (y/n): ")
    if again == 'n':
        print("Thanks for playing!")
        break
    



