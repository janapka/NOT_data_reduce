from pyraf import iraf
import string
import os
import sys


myTrimSection = "[100:1000,100:1000]"

os.system('dfits ../raw/*fits | fitsort object detxbin | grep "bias" > biasList.lis')
os.system('nedit biasList.lis')
iraf.noao()
iraf.imred()
iraf.ccdred()
iraf.zerocombine("@biasList.lis//[1]",output="../reduced/mybias",combine="median",reject="none",ccdtype="")
iraf.ccdproc("../reduced/mybias",output="../reduced/bias",ccdtype="",fixpix="no",overscan="no",trim="yes",zerocor="no",darkcor="no",flatcor="no",zero="bias", trimsec=myTrimSection)
