#!/usr/bin/env python3
#Michael Sims Script for Image Manipulation

from PIL import Image
from glob import glob
import os

#rotate and resize images through function
for file in glob('*.tiff'):
    im = Image.open(file)
    im.rotate(270).resize((128,128))
    #split off extension and add jpeg
    filename = file.split(".")[0] + ".jpeg"
    im.save('.../opt/icons/{}'.format(filename))

print('Done')
#check 
