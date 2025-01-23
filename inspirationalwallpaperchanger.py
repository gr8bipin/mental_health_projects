## Description: A program to set a motivational wallpaper each day.

## How it works:
# Store a folder of wallpapers.
# Use os or ctypes to change the desktop background.

# Example (Windows):

import ctypes
import os

# Ensure the file exists and use absolute path
wallpaper_path = os.path.abspath("BruceLee.JPG")

# Check if file exists before setting wallpaper
if os.path.exists(wallpaper_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaper_path, 0)
else:
    print(f"Wallpaper file not found: {wallpaper_path}")