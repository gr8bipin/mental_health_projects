# Self-Care Checklist

#Description: Create a checklist where users can mark daily self-care tasks (e.g., drinking water, exercising).

## How it Works:
# Display a list of self-care activities.
# Ask the user to input "yes" or "no" for each activity.
# Calculate the percentage of completed tasks.

tasks = ["Drink water", "Exercise", "Meditate", "Sleep 8 hours"]
completed = 0

for task in tasks:
    answer = input(f"Did you {task}? (yes/no): ").lower()
    if answer == "yes":
        completed += 1

print(f"You completed {completed}/{len(tasks)} tasks today!")