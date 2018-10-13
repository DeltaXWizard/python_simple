from random import randint 
from time import sleep

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
    else:
        print ("Rolling...")
        sleep(2)
        print (first_roll)
        sleep(1)
        print (second_roll)
        sleep(1)
        total_roll = first_roll + second_roll
        print("Result...")
        sleep(1)
        if total_roll == guess:
            print("Congratulations! You win!")
        else:
            print("Bad luck! You sadly lost :<")

roll_dice(6) #Traditional die pieces
