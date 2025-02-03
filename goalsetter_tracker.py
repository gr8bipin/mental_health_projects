###Goal Setter and Tracker

# Concept: Allows the user to set mental-related goals (e.g., "Meditate for 10 minutes daily"), track progress, and view their progress.

# Python skills: Lists, dictionaries, file I/O (to save goals), loops, conditional statements.

import json #Import the json module for handling JSON data.

def save_goals(goals):
    with open("goals.json", "w") as f: #Takes a dictionary goals as input. 
        json.dump(goals, f)

def load_goals():
    try:
        with open("goals.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}         

goals = load_goals()

while True:
    print("\nGoal Setter Menu:")
    print("1. Set a goal")
    print("2. Mark goal as complete")
    print("3. View goals")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
        goal_name = input("Enter your goal: ")
        goals[goal_name] = False # Initially incomplete
        save_goals(goals)
    elif choice == "2":
        goal_name = input("Enter the goal to mark as complete: ")
        if goal_name in goals:
            goals[goal_name] = True
            save_goals(goals)
        else:
            print("Goal not found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

