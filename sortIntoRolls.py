"""
Yet another script to sort the pictures into rolls?

TODO: Check with Raghu what we used to use this for.
"""
import os, os.path, shutil, re, sys

#the path to the sorted folder is to be entered here
#the sorted folders; folders, which contain !renamed! images
#remember to escape the backslashes if using windows
inputFolder = "/home/favre49/Documents/Oasis/Oasis/Unsorted/Sapnupuas/100D5300"

#create an output folder and input the path here
#if you have to run the script again, delete
#all files in this folder before running
#remeber, the output folder cant be inside the input folder
outputFolder = "/home/favre49/Documents/Oasis/Oasis/Uploaded"

rollnum = 186
os.mkdir(outputFolder+"/"+str(rollnum)+"R")

for file in sorted(os.listdir(inputFolder)):
    fileDir = inputFolder+"/"+file
    if not os.path.isdir(fileDir):
        picnum=int(re.split("[._]", file)[1])
        print(picnum)
        shutil.copy(fileDir, outputFolder+"/"+str(rollnum)+"R")
        if picnum%40 == 0:
            rollnum=rollnum+1
            os.mkdir(outputFolder+"/"+str(rollnum)+"R")
        if rollnum == 191:
            sys.exit()
