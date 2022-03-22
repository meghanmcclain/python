#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.
# you need png logo image called catlogo.png

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_SQUARE_FIT_SIZE = 60
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# Check if logo needs to be resized.
if logoWidth > LOGO_SQUARE_FIT_SIZE and logoHeight > LOGO_SQUARE_FIT_SIZE:
    # Calculate the new width and height to resize to.
    if logoWidth > logoHeight:
        logoHeight = int((LOGO_SQUARE_FIT_SIZE / logoWidth) * logoHeight)
        logoWidth = LOGO_SQUARE_FIT_SIZE
    else:
        logoWidth = int((LOGO_SQUARE_FIT_SIZE / logoHeight) * logoWidth)
        logoHeight = LOGO_SQUARE_FIT_SIZE

    # Resize the logo.
    print('Resizing %s...' % (logoIm))
    logoIm = logoIm.resize((logoWidth, logoHeight))

os.makedirs('withLogo', exist_ok=True) #create a withLogo folder to store the finished images
# Loop over all files in the working directory.
for filename in os.listdir('.'): #get a list of all files in cwd
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue #skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    # Add the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))
