import random


def guessnumb():
    # numb = the number that is randomly selected
    # user_guess = the numb that the user guessed
    # prev_guesses = the list of previous guesses the user made
    # count = used to go through prev_guesses to check for repeats

    # get new number and prompt user to make a guess
    numb = random.randint(1, 51)
    max_numb = 50
    min_numb = 1
    user_guess = int(input("Enter what you think the next number is (1-50). Enter 0 to stop playing. " +
                           "Enter -1 for a new number: "))

    # keep having user enter new number until satisfied with number (no enter -1)
    while user_guess == -1:
        numb = random.randint(1, 51)
        user_guess = int(input("Enter what you think the next number is (1-50). Enter 0 to stop playing. " +
                               "Enter -1 for a new number: "))
    # if user inputs 0, exit program
    if user_guess == 0:
        return

    # if numb is too large or too small (but is not 0 or -1), keep prompting to input
    while not checkrange(user_guess, max_numb, min_numb):
        user_guess = int(input("Number was too big or small. Please enter a new one: "))

    prev_guesses = []
    count = 0

    # if user enters 0, exit game
    while user_guess != 0:
        while user_guess != numb and user_guess != 0 and user_guess != -1:
            # goes through prev_guesses and checks if user typed in a repeat number
            while count < len(prev_guesses):
                # if there's a repeat number, prompt for a new number and go through list from begin
                if user_guess == prev_guesses[count]:
                    user_guess = int(input("You already tried that number, try again: "))
                    # if numb is too large or too small (but is not 0 or -1), keep prompting to input
                    while not checkrange(user_guess, max_numb, min_numb):
                        user_guess = int(input("Number was too big or small. Please enter a new one: "))
                    count = 0
                else:
                    count += 1

            # check where user_guess is in relation to numb
            if user_guess > numb:
                print("You're too high")
            elif user_guess < numb:
                print("You're too low")
            # if user guessed correctly, break out of while to keep user guessing
            else:
                break

            # if no correct, add user_guess to prev_guesses and prompt user
            prev_guesses.append(user_guess)
            user_guess = int(input("Try next number. Enter 0 to stop playing. Enter -1 for a new number: "))
            # if numb is too large or too small (but is not 0 or -1), keep prompting to input
            while not checkrange(user_guess, max_numb, min_numb):
                user_guess = int(input("Number was too big or small. Please enter a new one: "))
            count = 0

        # If the user guessed the correct number, say yeet then go on to next number
        if user_guess == numb:
            print("yeEEeEEeEEeettT")
        # if user enter 0, exit
        elif user_guess == 0:
            break
        # if user enter -1, get a new number
        elif user_guess == -1:
            print("Fetching new number...\n")

        # get new number and prompt user to make a guess
        numb = random.randint(1, 51)
        user_guess = int(input("Enter what you think the next number is (1-50). Enter 0 to stop playing. " +
                               "Enter -1 for a new number: "))

        # keep having user enter new number until satisfied with number (no enter -1)
        while user_guess == -1:
            numb = random.randint(1, 51)
            user_guess = int(input("Enter what you think the next number is (1-50). Enter 0 to stop playing. " +
                                   "Enter -1 for a new number: "))
        # if numb is too large or too small (but is not 0 or -1), keep prompting to input
        while not checkrange(user_guess, max_numb, min_numb):
            user_guess = int(input("Number was too big or small. Please enter a new one: "))

        prev_guesses = []
        count = 0


# checks if user_numb is within max_numb and min_numb
# returns True if in range or = 0 or -1, False if out of range
def checkrange(user_numb, max_numb, min_numb):
    if user_numb == 0 or user_numb == -1:
        return True
    elif user_numb > max_numb or user_numb < min_numb:
        return False
    else:
        return True


print("Whale cum!")
guessnumb()
print("Thank you for playing!")
