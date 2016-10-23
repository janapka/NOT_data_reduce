from pyraf import iraf
import string
import os
import sys

inputFile = sys.argv[1]

rawDir = "../raw/"
reducedDir = "../reduced/"
myTrimSection = "[100:1000,100:1000]"

os.system('dfits ' + inputFile + '| fitsort fafltnm > filter.tmp')
          
os.system('dfits ' + inputFile + '| fitsort tcstgt > tgt.tmp')
                    
filterFile = open("filter.tmp","r")
line = filterFile.readline()
#print line
line = filterFile.readline()
#print line
eachItem = string.split(string.strip(line))
#print eachItem[1]

fileName = inputFile[7:]
print fileName

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