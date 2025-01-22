#Overview: Make a simple text-based program where users answer questions, and the program suggests stress-relief techniques.

##Steps:
# Create a series of yes/no questions (e.g., "Are you feeling overwhelmed?").
# Use conditional statements to provide suggestions like deep breathing or journaling.

print("Stress Check - Answer 'yes' or 'no'")

question1 = input("Are you feeling overwhelmed? ").lower()
question2 = input("Do you find it hard to concentrate? ").lower()

if question1 == "yes" or question2 == "yes":
    print("Try taking deep breaths or journaling your thoughts.")
else:
    print("Keep up the great work maintaining balance!")