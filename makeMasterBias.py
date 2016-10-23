from pyraf import iraf
import string
import os
import sys
'''
The script needs dfits and fitsort routines installed. Combine is median to make it more robust.
Bias is one of the accessible keywords in the fits header. 
'''

myTrimSection = "[100:1000,100:1000]" #to remove low quality data from the edges

os.system('dfits ../raw/*fits | fitsort object detxbin | grep "bias" > biasList.lis')
os.system('nedit biasList.lis')
iraf.noao()
iraf.imred()
iraf.ccdred()
iraf.zerocombine("@biasList.lis//[1]",output="../reduced/mybias",combine="median",reject="none",ccdtype="")
iraf.ccdproc("../reduced/mybias",output="../reduced/bias",ccdtype="",fixpix="no",overscan="no",trim="yes",zerocor="no",darkcor="no",flatcor="no",zero="bias", trimsec=myTrimSection)
