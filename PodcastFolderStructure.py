# PodcastFolderStructure
"""
This is automating the creation of a folder structure for podcasts. 
It includes subfolders for each episodes. 
You can set the number of episode folders you want in line 25.
You can also set it to create episode folders that do not start from zero,
using the range(start number, number of folders) instead of range(number of folders)

"""
import os

# Declaring the folder names
project = input("Enter Podcast Name: ")
episode = "Episode "
finalAudio = "Final Audio"
rawElements = "Raw Elements"
showNotes = "Show Notes"
audiograms = "Soundbites/Audiograms"
graphics = "Graphics"
generalAssets = "General Assets"

root = "."

# For Loop to create multiple episodes and subfolders in range(s)
for s in range(20):
    path = f"{root}/{project}/{episode}{s}"
    path1 = f"{root}/{project}/{episode}{s}/{finalAudio}"
    path2 = f"{root}/{project}/{episode}{s}/{rawElements}"
    path3 = f"{root}/{project}/{episode}{s}/{showNotes}"
    path4 = f"{root}/{project}/{episode}{s}/{audiograms}"
    path5 = f"{root}/{project}/{episode}{s}/{graphics}"
    # Creating the directories
    os.makedirs(path)
    os.makedirs(path1)
    os.makedirs(path2)
    os.makedirs(path3)
    os.makedirs(path4)
    os.makedirs(path5)
    # Check if number of Episodes is correct
    print(path)
# Create General Assets folder in the project folder
path6 = f"{root}/{project}/{generalAssets}"
os.makedirs(path6)
