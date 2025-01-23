#Description: Ask the user how they feel and display an emoji based on their response.

##How it works:
#Map user input (happy, sad, angry, etc.) to an emoji.
#Use the emoji library to display emojis.

import emoji

mood = input("How are you feeling today? (happy/sad/angry): ").lower()

mood_emoji = {
    "happy": emoji.emojize(":grinning_face:"),
    "sad": emoji.emojize(":crying_face:"),
    "angry": emoji.emojize(":angry_face:")
}

print(f"Your mood: {mood_emoji.get(mood, 'unknown mood')}")