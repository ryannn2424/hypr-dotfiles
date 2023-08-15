#!/usr/bin/env python
import random
import subprocess
import os

wallpaper_dir = "~/Pictures/wallpapers/"
wallpapers = [
    "city.png",
    "forest.jpg",
    "land.jpg",
    "street.png"
]

# Get the current wallpaper from SWWW
current_info = subprocess.run(["swww", "query"], stdout=subprocess.PIPE).stdout
current_info = current_info.decode('utf-8')

# Chop down name
current_info = current_info[87:len(current_info)-1]
# print(current_info)

while True:
    #attempt to pick new wallpaper
    candidate_wallpaper = wallpapers[random.randint(0,3)]

    #Checks to see if wallpaper is current
    if candidate_wallpaper == current_info:
        print("Same Wallpaper!! Rerolling...")
    else:
        print("No matches found. Changing wallpaper..")
        break

final_path = wallpaper_dir + candidate_wallpaper

os.system("swww img " + final_path)