Series of scripts to reduce data from the Nordic Optical Telescope @La Palma.
The scripts require pyraf, dfits and fitsort routines (by ESO).

makeMasterBias.py    Creates BIAS frame
makeMasterFlats.py   Creates flat files for every filter
SExtractmany.py	     Runs SExtractor on all files. Needs SExtractor installed
reduceScience.py     Fully reduce scientific frame
reduceManyScience.py Reduces scientific images in bulk, uses reduceScience script.

Step-by-step

1) Create bias frame (makeMasterBias)
2) Create flat fields (makeMasterFlats)
3) Create reduced image (reduceScience)

It's better to then run the reduceScience in a for cycle as a bash one liner. 
