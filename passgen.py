### A simple password generator.

import random


def on_ready():  # For looping sakes.
    length = input("How long do you want your password to be?")
    length = int(length)
    return selection(length)


def selection(length):
    suggestion = input("How many passwords would you like to choose from?")
    s = int(suggestion)
    return main(length, s)


def main(length, s):  # MUST execute first
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"

    for p in range(s):
        password = ''
        for c in range(length):
            password += random.choice(chars)
        print(password)


on_ready()
