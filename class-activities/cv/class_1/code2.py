import os
import sys
sys.path.append(os.getcwd().split('/PDI')[0])
import numpy as np
from PDI.src.pdi_utils import load_flipped_seville, show_image

flipped_seville = load_flipped_seville()

# Show original image
show_image(flipped_seville, 'Seville Flipped')

# Flip the image vertically
seville_vertical_flip = flipped_seville[::-1,:]

# Show image flippped vertically
show_image(seville_vertical_flip, 'Seville Vertical Flipped')

# Flip the image horizontally
seville_horizontal_flip = seville_vertical_flip[:, ::-1]

# Show image flipped horizontally
show_image(seville_horizontal_flip, 'Seville horizontal Flipped')