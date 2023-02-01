#! python3
import os
from PIL import Image
from pathlib import Path

p=Path.cwd()
for foldername, subfolders, filenames in os.walk(p):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (filename.endswith('.png') or filename.endswith('.jpg')):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        fileimag = Image.open(filename)
        fileimagwidth, fileimagheight = fileimag.size

        # Check if width & height are larger than 500.
        if fileimagheight>500 and fileimagwidth>500:
            # Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            # Image is too small to be a photo.
            numNonPhotoFiles += 1
    if numPhotoFiles>numNonPhotoFiles:
        print(os.path.abspath(foldername))
    # If more than half of files were photos,
    # print the absolute path of the folder.