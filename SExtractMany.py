from pyraf import iraf
import string
import os
import sys

rawDir = "../raw/"
reducedDir = "../reduced/"
myTrimSection = "[100:1000,100:1000]"

os.system("ls " + reducedDir + "r*.fits > myList.tmp")

myListFile = open("myList.tmp","r")

for eachLine in myListFile:
    print eachLine
    inputFile = string.strip(eachLine)
    print inputFile
    
    if os.path.exists(inputFile.replace(".fits",".cat")):
        print "this file has already been SExtracted"
    else:
        command = "sex  " + inputFile
        print command
        os.system(command)
        command = "mv red.cat "+ inputFile.replace(".fits",".cat")
        print command
        os.system(command)

myListFile.close()
