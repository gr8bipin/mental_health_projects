#  Breathing Exercise Timer:

# Concept: Guides the user through paced breathing exercises (e.g., 4-7-8 breathing).
# Python Skills: time module (for pauses), loops, basic output.

import time

def breathing_exercise(inhale_time, hold_time, exhale_time, repetitions):

    """Guides the user through a paced breathing exercise."""  # Docstring for clarity
    if not isinstance(repetitions, int) or repetitions <= 0:
        print("Invalid number of repetitions. Please enter a positive integer.")
        return  # Exit the function if input is invalid

    for i in range(repetitions):
        print(f"Repetition {i+1}:") # Indicate which repetition it is
        print("Inhale...")
        time.sleep(inhale_time)
        print("Hold...")
        time.sleep(hold_time)
        print("Exhale...")
        time.sleep(exhale_time)
        print()  # Add an empty line for better readability

try:
    num_repetitions = int(input("How many repetitions? "))
    breathing_exercise(4, 7, 8, num_repetitions) # 4-7-8 breathing
    
    print("Exercise complete.")
except ValueError:
    print("Invalid input. Please enter a number for the repetitions.")
