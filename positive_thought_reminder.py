#  Positive Thought Reminder

# Description: Create a script that sends motivational or positive messages at regular intervals.

## How it Works:
# Use the time or schedule library to set reminders.
# Display positive quotes in the console or send notifications.

import time

quotes = [
    "Believe in yourself!",
    "You are stronger than you think.",
    "Take one step at a time.",
    "You are doing great!"
]

for quote in quotes:
    print(quote)
    time.sleep(10)  # Wait 10 seconds before the next message