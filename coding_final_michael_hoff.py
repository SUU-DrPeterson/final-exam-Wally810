"""This program selects a number 1 through 100 and has the user try and guess it."""
#Michael Hoff

import random

#Keeps the programming looping indefinitely until input at the end alters KEEP_RUNNING to false
KEEP_RUNNING = True
while KEEP_RUNNING:

    #Gets the user input and calls the respective functions.
    def get_values():
        """This function prompts the user to choose an input for the function to run."""

        #Asks the user which input for the function they'd like to run.
        ask_program = str(input('\nWhich program would you like to run?'
                                '\n1. Try and guess an integer 1 through 10. (Easy)'
                                '\n2. Try and guess an integer 1 through 100. (Medium)'
                                '\n3. Try and guess a two decimal number 1 through 100. (Hard)'
                                '\n'))

        #If the user inputs '1', function_one is called.
        if ask_program == '1':
            function_one()

        #If the user inputs '2', function_two is called.
        elif ask_program == '2':
            function_two()

        #If the user inputs '2', function_two is called.
        elif ask_program == '3':
            function_three()

        #If the user inputs anything else, they're informed its an invalid response
        else:
            print('That is not a valid response.')



    #function_one is called to have the user select an integer from 1-10 until correct.
    def function_one():
        """Randomly selects an integer from 1 to 10 and has the user guess until correct."""

        #Random int between 1-10 is assigned, empty list is created, and guess counter is
        #initialized.
        random_number = random.randint(1, 10)
        guessed_numbers = []
        guess_tally = 0

        print('A random integer from 1 to 10 has been selected.\n')

        #While loop until correct guess is given.
        keep_guessing = True
        while keep_guessing:

            #Trys asking for an int and excepts if wrong input
            try:
                user_guess = int(input('Please enter your guess: '))
            except TypeError:
                print("Error: You didn't enter a number.")

            #If the answer is the same as the random int, the while loop is ended and a
            #congratulations message is printed.
            if user_guess == random_number:
                keep_guessing = False
                if guess_tally == 1:
                    print('\nCongratulations, you guessed correctly after', guess_tally, 'try!')
                else:
                    print('\nCongratulations, you guessed correctly after', guess_tally, 'tries!')
                break

            #If the guess is over 10 or below 1, an out of bounds message is printed
            if user_guess > 10 or user_guess < 1:
                print('\nThis number is out of bounds, please choose between 1 and 10.')

            #Else, the code determines if the guess has been give before.
            else:

                #If the guess us in the guessed numbers list, the user is informed if its too high
                #or not and that its been guessed before
                if user_guess in guessed_numbers:
                    if user_guess > random_number:
                        print('\nThis number has already been guessed and is too high.')
                    elif user_guess < random_number:
                        print('\nThis number has already been guessed and is too low.')

                #If the guess hasn't been guessed before, the user is just informed if its too high
                #or not
                else:
                    if user_guess > random_number:
                        print('\nThis number is too high.')
                    elif user_guess < random_number:
                        print('\nThis number is too low.')

            #If the guess isn't in the list of guessed numbers, its added, then the list is sorted
            if user_guess not in guessed_numbers:
                guessed_numbers.append(user_guess)
                guessed_numbers.sort()

            #Tally of guesses goes up by one
            guess_tally += 1

            #The list of already guessed numbers is printed
            print('\nAlready guessed numbers:', guessed_numbers)



    #function_two is called to have the user select an integer from 1-100 until correct.
    def function_two():
        """Randomly selects an integer from 1 to 100 and has the user guess until correct."""

        #Random int between 1-100 is assigned, empty list is created, and guess counter is
        #initialized.
        random_number = random.randint(1, 100)
        guessed_numbers = []
        guess_tally = 0

        print('A random integer from 1 to 100 has been selected.\n')

        #While loop until correct guess is given.
        keep_guessing = True
        while keep_guessing:

            #Trys asking for an int and excepts if wrong input
            try:
                user_guess = int(input('Please enter your guess: '))
            except TypeError:
                print("Error: You didn't enter a number.")

            #If the answer is the same as the random int, the while loop is ended and a
            #congratulations message is printed.
            if user_guess == random_number:
                keep_guessing = False
                if guess_tally == 1:
                    print('\nCongratulations, you guessed correctly after', guess_tally, 'try!')
                else:
                    print('\nCongratulations, you guessed correctly after', guess_tally, 'tries!')
                break

            #If the guess is over 100 or below 1, an out of bounds message is printed
            if user_guess > 100 or user_guess < 1:
                print('\nThis number is out of bounds, please choose between 1 and 100.')

            #Else, the code determines if the guess has been give before.
            else:

                #If the guess us in the guessed numbers list, the user is informed if its too high
                #or not and that its been guessed before
                if user_guess in guessed_numbers:
                    if user_guess > random_number:
                        print('\nThis number has already been guessed and is too high.')
                    elif user_guess < random_number:
                        print('\nThis number has already been guessed and is too low.')

                #If the guess hasn't been guessed before, the user is just informed if its too high
                #or not
                else:
                    if user_guess > random_number:
                        print('\nThis number is too high.')
                    elif user_guess < random_number:
                        print('\nThis number is too low.')

            #If the guess isn't in the list of guessed numbers, its added, then the list is sorted
            if user_guess not in guessed_numbers:
                guessed_numbers.append(user_guess)
                guessed_numbers.sort()

            #Tally of guesses goes up by one
            guess_tally += 1

            #The list of already guessed numbers is printed
            print('\nAlready guessed numbers:', guessed_numbers)



    #function_three is called to have the user select a two decimal number from 1-100 until correct.
    def function_three():
        """Randomly selects a two decimal number from 1 to 100, has the user guess until correct."""

        #Random two decimal number between 1-100 is assigned, empty list is created, and guess
        #counter is initialized.
        random_number = round(random.uniform(0, 100), 2)
        guessed_numbers = []
        guess_tally = 0

        print('A random two decimal number from 1 to 100 has been selected.\n')

        #While loop until correct guess is given.
        keep_guessing = True
        while keep_guessing:

            #Trys asking for an int and excepts if wrong input
            try:
                user_guess = float(input('Please enter your guess: '))
            except TypeError:
                print("Error: You didn't enter a number.")

            #If the answer is the same as the random int, the while loop is ended and a
            #congratulations message is printed.
            if user_guess == random_number:
                keep_guessing = False
                if guess_tally == 1:
                    print('\nCongratulations, you guessed correctly after', guess_tally, 'try!')
                else:
                    print('\nCongratulations, you guessed correctly after', guess_tally, 'tries!')
                break

            #If the guess is over 100 or below 1, an out of bounds message is printed
            if user_guess > 100 or user_guess < 1:
                print('\nThis number is out of bounds, please choose between 1 and 100.')

            #Else, the code determines if the guess has been give before.
            else:

                #If the guess us in the guessed numbers list, the user is informed if its too high
                #or not and that its been guessed before
                if user_guess in guessed_numbers:
                    if user_guess > random_number:
                        print('\nThis number has already been guessed and is too high.')
                    elif user_guess < random_number:
                        print('\nThis number has already been guessed and is too low.')

                #If the guess hasn't been guessed before, the user is just informed if its too high
                #or not
                else:
                    if user_guess > random_number:
                        print('\nThis number is too high.')
                    elif user_guess < random_number:
                        print('\nThis number is too low.')

            #If the guess isn't in the list of guessed numbers, its added, then the list is sorted
            if user_guess not in guessed_numbers:
                guessed_numbers.append(user_guess)
                guessed_numbers.sort()

            #Tally of guesses goes up by one
            guess_tally += 1

            #The list of already guessed numbers is printed
            print('\nAlready guessed numbers:', guessed_numbers)





    #This calls the getValues() function that runs and asks the user which of the other
    #functions they'd like to run
    get_values()





    #Second KEEP_RUNNING while loop asking if the user would like to continue
    KEEP_RUNNING_2 = True
    while KEEP_RUNNING_2:

        #Asks the user a y/n question whether they'd like to continue
        ASK_CONTINUE = str(input('\nWould you like to run another program? y/n\n')).lower()

        #If 'n', both KEEP_RUNNING variables turn false, ending both loops
        if ASK_CONTINUE == 'n':
            KEEP_RUNNING = False
            KEEP_RUNNING_2 = False

        #If 'y', only the second KEEP_RUNNING variable turns false, ending this while loop
        elif ASK_CONTINUE == 'y':
            KEEP_RUNNING_2 = False

        #If any other value is entered, the user is informed its an invalid reponse.
        else:
            print('That is not a valid response.')



#This assignment helped to familiarize me random function and the way it works. I also used
#the assignment as a test in implementing things via thinking "What would I, as the user, most
#appreciate while using this program" and then implementing those things. For example, while
#working on the "medium" difficulty, I was having some issue remembering which numbers I used
#before so I added the guessed numbers list. Then, while working on the "hard" difficulty, I
#kept losing track in the decimal numbers which guesses were higher or lower, so I rewrote
#the "This number has been guessed already" code to also display if that guess was too high
#or too low. This made the experience for me, as the user, much more enjoyable, and helped
#when introducing various "quality of life" changes to my program.
