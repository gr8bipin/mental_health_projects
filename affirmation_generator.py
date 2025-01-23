#Algorithm:

# Store a list of affirmations.
# Generate a random index within the range of the list's length.
# Retrieve the affirmation at that random index.
# Display the affirmation.

import random

affirmations = [
    "I am worthy of love and happiness.",
    "I am capable of achieving my goals.",
    "I am strong and resilient.",
    "I believe in myself.",
    "I am grateful for all the good in my life.",
    "Every day is a fresh start.",
    "I choose peace and joy."
]

def generate_affirmation():
    random_index = random.randint(0, len(affirmations) - 1)
    return affirmations[random_index]

def add_affirmation():
    new_affirmation = input("Enter a new affirmation: ")
    affirmations.append(new_affirmation)
    print(affirmations)
    print("Affirmation added!")

while True:
    print("\nAffirmation Generator Menu:")
    print("1. Generate an affirmation")
    print("2. Add an affirmation")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print(generate_affirmation())
    elif choice == '2':
        add_affirmation()
    elif choice == '3':
        break
    else:
        print("Invalid Choice. Please try again.")
