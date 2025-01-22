##Overview: Create a program that displays a random positive affirmation every time it is run.

# Steps:
# Use a list of affirmations (e.g., "You are capable!", "Today will be a great day!").
# Use Python's random.choice() to select one affirmation.
# Print the affirmation to the console.

import random

affirmations = [
    "You are capable of amazing things!",
    "Today is a fresh start.",
    "You are loved and appreciated.",
    "You are stronger than you think.",
    "Take it one step at a time."
]

print("Your affirmation for today:")
print(random.choice(affirmations))