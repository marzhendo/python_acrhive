import imageio.v3 as iio

filenames = ['pic-1.jpeg', 'pic-3.jpeg']
images = [ ]
for filename in filenames:
    images.append(iio.imread(filename))

# turn the image into a gif
iio.imwrite('KoalaKalibening.gif', images, duration = 500, loop = 0)
