from pyraf import iraf
import string
import os
import sys

rawDir = "../raw/"
reducedDir = "../reduced/"
myTrimSection = "[100:1000,100:1000]"

os.system('dfits ' + rawDir +'*fits | fitsort object fafltnm | grep "FLAT" > flatsList.lis')
#os.system('nedit flatsList.lis')
gFlats = open("gflats.lis","w")
rFlats = open("rflats.lis","w")
iFlats = open("iflats.lis","w")

bgFlats = open("bgflats.lis","w")
brFlats = open("brflats.lis","w")
biFlats = open("biflats.lis","w")

allFlats = open("flatsList.lis","r")
for eachLine in allFlats:
    eachItem = string.split(string.strip(eachLine))
    print eachLine
    if "g" in eachItem[-2]:
        #print eachItem[0][7:]
        gFlats.write(rawDir + eachItem[0][7:]+"\n")
        bgFlats.write(reducedDir + "b" + eachItem[0][7:]+"\n")
    if "r" in eachItem[-2]:
        #print eachItem[0][7:]
        rFlats.write(rawDir + eachItem[0][7:]+"\n")
        brFlats.write(reducedDir + "b" + eachItem[0][7:]+"\n")
    if "i" in eachItem[-2]:
        #print eachItem[0][7:]
        iFlats.write(rawDir + eachItem[0][7:]+"\n")
        biFlats.write(reducedDir + "b" + eachItem[0][7:]+"\n")
gFlats.close()
rFlats.close()
iFlats.close()

bgFlats.close()
brFlats.close()
biFlats.close()

iraf.noao()
iraf.imred()
iraf.ccdred()
iraf.ccdproc("@gflats.lis//[1]",output="@bgflats.lis",ccdtype="",fixpix="no",overscan="no",trim="yes",zerocor="yes",darkcor="no",flatcor="no",zero="../reduced/bias", trimsec=myTrimSection)
iraf.flatcombine("@bgflats.lis",output="gflat",ccdtype="",process="no",subsets="no")

iraf.ccdproc("@rflats.lis//[1]",output="@brflats.lis",ccdtype="",fixpix="no",overscan="no",trim="yes",zerocor="yes",darkcor="no",flatcor="no",zero="../reduced/bias", trimsec=myTrimSection)
iraf.flatcombine("@brflats.lis",output="rflat",ccdtype="",process="no",subsets="no")

iraf.ccdproc("@iflats.lis//[1]",output="@biflats.lis",ccdtype="",fixpix="no",overscan="no",trim="yes",zerocor="yes",darkcor="no",flatcor="no",zero="../reduced/bias", trimsec=myTrimSection)
iraf.flatcombine("@biflats.lis",output="iflat",ccdtype="",process="no",subsets="no")
