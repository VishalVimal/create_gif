#Create GIF in python with just 6 lines 

# Import the imageio library for reading and writing images
import imageio.v3 as iio 

# List of filenames for the images to be included in the GIF
filenames = ['images/nature1.png','images/nature2.png']

# Initialize an empty list to store the images
images = [] 

# Loop through each filename and read the image
for filename in filenames:
    images.append(iio.imread(filename))

# Write the images to a GIF file with specified duration and loop count
iio.imwrite('Output/nature.gif', images, duration=500, loop=0)
