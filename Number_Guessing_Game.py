import random

def random_number(lower_bound, upper_bound):# Generates random number
    """Generate a random number between lower_bound and upper_bound."""
    generated_number = random.randint(lower_bound, upper_bound) # Gets random number  from the range of values defined by lower_bound and upper_bound
    return generated_number # Returns random number

def guess_number(): # Function to get integer input
    """Get a valid  integer input from the user."""
    while True: # Loop until valid input is received
        try:
            user_guess = int(input("Please enter a number: ")) # Get user input
            return user_guess # Return input if it's a number
        except ValueError:
            print("Invalid input. Please enter a number.") # Print error message if input is not a number

def input_trial(): # Function to positive user trial
    """Get a valid positive integer input from the user for the number of trials."""
    while True: # Loop until valid input is received
        try:
            trial = int(input("Please enter how many tries you would like to have: ")) # Get user input
            if trial > 0:
                return trial
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")

def guess_checker(generated_number, trial):
    """Check the user's guess against the generated number."""
    for i in range(trial, 0, -1):
        guess = guess_number()
        if guess > generated_number:
            print("Too high.")
        elif guess < generated_number:
            print("Too low.")
        elif guess == generated_number:
            print("Congratulations! You guessed the number.")
            return
    print(f"The number was not the right one. The correct number is {generated_number}.")

def main():
    print("Welcome to the Number Guessing Game!")
    print('Please  follow these simple rules:\n')
    print('- The computer will think of an integer between lowerbound and Upperbound of your entry.\n')
    print('- You need to guess what this number is by entering your own integer each time\n')
    print('You get as your desired attempts to know the number. But, If you run out of attempts,\n')
    print('the computer will reveal the correct number.')

    """Get a valid positive lowerbound from the user to generate random numbers."""
    while True:
        try:
            lowerbound = int(input("Please enter lowerbound of the interval: "))
            upperbound = int(input("Please enter upperbound of the interval: "))
            if lowerbound >= upperbound:
                print("Lowerbound cannot be greater than or equal to upperbound.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter integers only.")
    
    
    generated_number = random_number(lowerbound,upperbound)
    trial = input_trial()
    guess_checker(generated_number, trial)

if __name__ == "__main__":
    main()