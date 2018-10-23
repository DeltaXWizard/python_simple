### A simple password generator.

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_-+={[}]|\:;\"'<,>.?/"

length = input("How long do you want your password to be?")
length = int(length)

suggestion = input("How many passwords would you like to choose from?")
s = int(suggestion)

for p in range(s):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)
