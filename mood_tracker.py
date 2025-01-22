# Mood Tracker (Console-Based)

##Overview: Create a program where users enter their mood daily, and the program saves it in a text file.
##Steps:
# Use input() to ask the user how they are feeling.
# Save their response along with the current date in a .txt file.

from datetime import datetime

mood = input("How are you feeling today? ")
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(r"C:\Users\bipinshr\mental_health_projects\mood_log.txt", "a") as file:
    file.write(f"{date} - {mood}\n")

print("Your mood has been logged. Have a great day!")