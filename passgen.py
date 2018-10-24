### A simple password generator.

import random
import itertools

from time import sleep

def on_ready():
    length = input("How long do you want your password to be?")
    length = int(length)
    return selection(length)


def selection(length):
    suggestion = input("How many passwords would you like to choose from?")
    s = int(suggestion)
    return main(length, s)


def main(length, s):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"
    password = ''

    for x in itertools.repeat(None, s):
        for c in range(length):
            password += random.choice(chars)

        print(password)
        password = ''

    return redo()

def redo():
    redo = input("Will you like to get more? Type yes to retry and no to exit. ")
    if redo == "yes":
        return on_ready()
    elif redo == "no":
        print("Going offline...")
        sleep(1)
        return
    else:
        print("Please either be yes or no.")

on_ready()
