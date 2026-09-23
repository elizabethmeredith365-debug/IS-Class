#play_again = "y"

#While user has pressed "y"
    # computer generates a random number

    # while the user has not guessed the number

        # Ask the user for a guess between 1 and 100

        # while the guess is < 1 or > 100 
            # print "invalid guess, please try again"

        # increment the number of guesses


        # If the guess is > the number
        #   print "lower"
        # If the guess is < the number
        #   print "higher"
        # if the guess is = the number 
        #   print "Congratulations!"

    # loop ends


    # print the number of guesses


    # If number of guesses is <= 3
        # print "You are amazing"
    # else if the number of guesses <= 5
    #   print "Impressive!"
    #Else if number of guesses <= 7
    #   Print "Good Job"
    # Else if number of guesses <= 9
    #   Print "took a liile longer, but you got it!"
    # Else if number of guesses > 10
    #   Print "You need to lock in"
    
    #ask user to press "y" if they want to play again

#Loop


import random

play_game = input("Would you like to play the game? (Y/N): ").upper()

while play_game == "Y":

    counter = 0

 # Generate Random number
    random_number = random.randint(1, 100) 

    users_number = int(input("Guess a number between 1 and 100: "))

    while users_number != random_number :

#Add to the counter every time the loop repeats, so you know the # of tries
        counter += 1

#Tell the user if the guess is right, too high, or too low
        if users_number > random_number:
            print("lower")
        elif users_number < random_number:
            print("higher")
        elif users_number == random_number:
            print("Congratulations!")
        else :
            print("invalid guess, please try again")

        users_number = int(input("Guess a number between 1 and 100: "))


#Print the results depending on how many tries it took
    if counter <= 3:
        print("Amazing!")
    elif counter <= 5:
        print("Impressive!")
    elif counter <= 7:
        print("Good Job!")
    elif counter <= 9:
        print("Took a little longer, but you got there!")
    elif counter > 9:
        print("You need to lock in.")

# End or repeat the loop
    play_game = input("Would you like to play the game? (Y/N): ").upper()

