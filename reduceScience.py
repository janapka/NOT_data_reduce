from pyraf import iraf
import string
import os
import sys
'''
Assume dfits and fitsort are installed on the machine. Fully reduces one scientific frame.
'''

inputFile = sys.argv[1]

rawDir = "../raw/"
reducedDir = "../reduced/"
myTrimSection = "[100:1000,100:1000]"

os.system('dfits ' + inputFile + '| fitsort fafltnm > filter.tmp') #gets the filter from NOT
#keyword  
#os.system('dfits ' + inputFile + '| fitsort tcstgt > tgt.tmp')
                    
filterFile = open("filter.tmp","r")
line = filterFile.readline()
#print line
line = filterFile.readline()
#print line
eachItem = string.split(string.strip(line))
#print eachItem[1]

fileName = inputFile[7:]
print fileName
#if the file already exists, pyraf crashes, hence need to check for it. It doesn't
#overwrite!
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

filterFile.close()
