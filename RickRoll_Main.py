import os
import shutil
import requests

rick=requests.get("https://media.unboxholics.com/media/source/Articles/82935/images/bigImage/rick-roll-in-4k.jpg")

image=rick.content

#Prepare the folder path and name
path=os.path.join(os.getcwd(),"RICK_ROLL")

#check if the directory exists and if does it deletes it and it's content
if os.path.exists(path):
    shutil.rmtree(path)

#Create a directory(folder) on the same location as the file
os.mkdir(path)

#How many image to create
times=int(input("Enter how many RickRoll pictures do you want to generate:"))
if times>50000:
    print("You may have to wait a litle depenting on yoursystem")

#Create the Rick Roll images
for i in range(times):
    with open(f"RICK_ROLL/RickRoll{i+1}.png" ,"wb") as newrick:
        newrick.write(image)
