##Random Self-Care Tip

## Overview: Display a random self-care tip when the program runs.

##Steps:
#Create a list of self-care tips (e.g., "Drink water", "Go for a walk").
#Use random.choice() to select a tip and display it.

import random

tips = [
    "Drink a glass of water.",
    "Take a 5-minute walk.",
    "Write down 3 things you're grateful for.",
    "Listen to your favorite song.",
    "Take a short break to stretch."    
]

print("Your self-care tip for today:")

print(random.choice(tips))