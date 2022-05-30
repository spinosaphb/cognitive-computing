import os
import sys
sys.path.append(os.getcwd().split('/PDI')[0])

import matplotlib.pyplot as plt
from PDI.src.pdi_utils import load_red_roses, show_image

image = load_red_roses()

# Show original image
show_image(image, 'image RGB')

# Obtain the red channel
red_channel = image[:, : , 0]

# Show original image
show_image(red_channel,'image red channel')

# Plot the red histogram with bins in a range of 256
plt.hist(red_channel.ravel(), bins=256)

# Set title and show
plt.title('Red Histogram')
plt.show()