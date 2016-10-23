Series of scripts to reduce data from the Nordic Optical Telescope @La Palma.
The scripts require pyraf.

makeMasterBias.py    Creates BIAS frame
makeMasterFlats.py   Creates flat files for every filter
SExtractmany.py	     Runs SExtractor on all files. Needs SExtractor installed
reduceScience.py     Fully reduce scientific frame
reduceManyScience.py Reduces scientific images in bulk, uses reduceScience script.
