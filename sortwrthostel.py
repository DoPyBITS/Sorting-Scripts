"""
Sort the pictures into their bhawans. Used for printing.

TODO: Check if this works.
"""
import os, os.path, shutil

#the path to the sorted folder is to be entered here
#the sorted folders; folders, which contain !renamed! images
#remember to escape the backslashes if using windows
inputFolder = "/home/favre49/Documents/OasisPhotobooth"

#create an output folder and input the path here
#if you have to run the script again, delete
#all files in this folder before running
#remeber, the output folder cant be inside the input folder
outputFolder = "/home/favre49/Documents/OasisSorted/Photobooth"

ctr = 0
for dirName, subdirList, fileList in os.walk(inputFolder):
    for fname in fileList:
        #check if the file is of required format put .jpg and .JPG here
        if fname.endswith('.jpg') or fname.endswith('.JPG'):
            #the folder path has been extracted assuming
            #that all but the last 4 characters of the last word
            #when the string is split with _ is the folder name
            #eg:- ..._13121.jpg and ..._M14089.jpg
            folderName = fname.split('_')[0]
            #check if folder already exists. if not create the folder
            #print (folderName+" " + dirName + " " + fname)
            #print(os.path.join(outputFolder, folderName))
            if not os.path.exists(os.path.join(outputFolder, folderName)):
                os.mkdir(os.path.join(outputFolder, folderName))
            #copy file from the input folder to the new path
            print(fname.split('_')[2] + " " + fname.split('_')[4])
            shutil.copy(os.path.join(dirName, fname), os.path.join(outputFolder, folderName))
    for subname in subdirList:
        print("Done For %s " %subname)
        ctr += 1
        print(ctr)

