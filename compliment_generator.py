## Compliment Generator

##Overview: Build a program that gives the user a random compliment to boost their mood.
##Steps:
#Create a list of compliments.
#Randomly display one each time the program runs.

import random

compliments = [
    "You have a great sense of humor!",
    "You are an amazing person!",
    "Your smile lights up the room.",
    "You are so creative!",
    "You are making a difference in the world."
]

print("Here's a compliment for you:")
print(random.choice(compliments))