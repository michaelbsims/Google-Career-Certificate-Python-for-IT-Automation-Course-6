#!/usr/bin/env python3
#Image Manipulator, path will be '~/supplier-data/images'
import os
from PIL import Image
path = '~/supplier-data/images'
for file in os.listdir(path):
    if '.tiff' in filename:
        img = Image.open(path+file).covert('RGB')
        dir, newfile = os.path.split(file)
        newfile = os.path.splitext(newfile)[0]
        img.resize((600,400))
        img.save(path + filename + '.jpeg' + 'jpeg')
