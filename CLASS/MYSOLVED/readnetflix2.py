# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "CLASS", "netflix_ratings.csv")

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    videoTitle = ""
    rating = ""
    userRating = ""

    # Loop through looking for the video
    for row in csvreader:
        if row[0] == video:
             videoTitle = row[0]
             rating = row[1]
             userRating = row[5]
             break
            
    # Check if video title is found
    if videoTitle != "":
        print(videoTitle + " is rated " + rating + " with a rating of" + userRating)
    else:
        print("Sorry about this, we don't seem to have what you are looking for!")
        
        
