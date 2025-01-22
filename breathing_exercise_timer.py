## Breathing Exercise Timer

## Overview: Create a program that guides uers through a simple breathing exercise.

## Steps:
# Use a loop to display instructions (e.g., "Breathe in...hold...breathe out") with a delay.)
# Use the time.sleep() function for timing.

import time

print("Let's do a simple breathing exercise.")

for i in range(3):
    print("Breathe in...")
    time.sleep(4)
    print("Hold your breath...")
    time.sleep(4)
    print("Breathe out...")
    time.sleep(4)
    print("Hold your breath...")
    time.sleep(4)

print("Great job! You completed your exercise.")