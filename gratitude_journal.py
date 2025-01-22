## Grtitude Journal

##Overview: Allow users to input things they're grateful for.

##Steps:
# Ask the user to input three things they're grateful for.
# Save the input in a .txt file.

print("Gratitude Journal:")

gratitude1 = input("What is the first thing you are grateful for? ")
gratitude2 = input("What is the second thing you are grateful for? ")
gratitude3 = input("What is the third thing you are grateful for? ")

with open("gratitude.txt", "a") as file:
    file.write(f"{gratitude1}\n{gratitude2}\n{gratitude3}")

print("Your gratitude has been saved. Have a wonderful day!")