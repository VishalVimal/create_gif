import imageio.v3 as iio 
filenames = ['images/nature1.png','images/nature2.png']
images = [] 
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('Output/nature.gif', images, duration=500, loop=0)

