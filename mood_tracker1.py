# Algorithm:

# Prompt the user to enter their mood (e.g., using a scale of 1-5 or emoticons).
# Store the mood data in a list.
# Calculate the average mood.
# Display the average mood.
# (Optional) Display a simple trend (e.g., "Mood has been generally improving/stable/declining").

moods = []

num_days = int(input("How many days of mood data do you want to enter? "))

for i in range(num_days):
    while True:
        try:
            mood = int(input(f"Enter your mood for day {i + 1} (1-5): "))
            if 1 <= mood <= 5:
                moods.append(mood)
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if moods: #Check if the list is not empty
    average_mood = sum(moods) / len(moods)
    print(f"Your average mood over the past {num_days} days is: {average_mood: .2f}")

    # Simple Trend Analysis
    if len(moods) > 2:
        if moods[-1] > moods[-2] and moods[-2] > moods[-3]:
            print("Mood has been generally improving.")
        elif moods[-1] < moods[-2] and moods[-2] < moods[-3]:
            print("Mood has been generally declining.")
        else:
            print("Mood has been relatively stable.")
else:
    print("No mood data entered.")