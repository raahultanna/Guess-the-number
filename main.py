# Guess the number

import random

no = random.randint(1,10)

for i in range(0,3):
    User = int(input("Guess the number:\n"))

    if User == no:
        print(f"""Congrats!!! \nYou have guessed the correct number {no}""") #f string for formatting f the string
        break
    else:
        print(f"You have guessed the incorrect number {no}")

