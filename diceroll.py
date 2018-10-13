from random import randint 
from time import sleep

def on_ready(): # For looping sakes.
    y = input("How big do you want your dice size to be? ")
    roll_dice(int(y))

def get_user_guess():
	guess = input("What is your guess? ")
	return int(guess)

def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides)
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2
    print ("Your maximum value is " + str(max_val))
    guess = get_user_guess()
    if guess > max_val:
        print ("Your guess is invalid.")
        redo = input("Will you like to play again? Type yes to retry and no to exit. ")
        if redo == "yes":
            return on_ready()
        elif redo == "no":
            print("Going offline...")
            sleep(1)
            return # experimental.
        else:
            print("Please either be yes or no.")
    else:
        print ("Rolling 2 die...")
        sleep(2)
        print (str(first_roll) + " is your first roll!")
        sleep(1)
        print (str(second_roll) + " is your second roll!")
        sleep(1)
        total_roll = first_roll + second_roll
        print("Result...")
        sleep(1)
        if total_roll == guess:
            print("Congratulations! You win!")
        else:
            print("Bad luck! You sadly lost :<\n\nThanks for playing... try again?")
            end = input("Will you like to play again? Type yes to retry and no to exit. ")
            if end == "yes":
                return on_ready()
            elif end == "no":
                print("Going offline...")
                sleep(1)
                return # experimental.
            else:
                print("Please either be yes or no.")


y = input("How big do you want your dice size to be? ") #default execution
roll_dice(int(y))
