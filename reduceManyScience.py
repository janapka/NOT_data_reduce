from pyraf import iraf
import string
import os
import sys

rawDir = "../raw/"
reducedDir = "../reduced/"
myTrimSection = "[100:1000,100:1000]"

os.system("ls " + rawDir + " *.fits > myList.tmp")

myListFile = open("myList.tmp","r")

for eachLine in myListFile:
    print eachLine
    inputFile = string.strip(eachLine)
    print inputFile
    
    command = "python reduceScience.py " + rawDir + inputFile
    os.system(command)

    print command

"""
if os.path.exists(reducedDir + "r" + fileName):
    sys.exit("file " + fileName + " has already been reduced")
else:

    iraf.noao()
    iraf.imred()
    iraf.ccdred()
    if 'g' in eachItem[1]:
        myflat = "gflat"
    if 'r' in eachItem[1]:
        myflat = "rflat"
    if 'i' in eachItem[1]:
        myflat = "iflat"
    print myflat
    iraf.ccdproc(inputFile+"[1]",output=reducedDir + "r" + fileName ,ccdtype="",fixpix="no",overscan="no",trim="yes",zerocor="yes",darkcor="no",flatcor="yes",zero="../reduced/bias",flat=myflat,trimsec=myTrimSection)
"""

myListFile.close()
