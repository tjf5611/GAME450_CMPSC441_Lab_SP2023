import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np

def get_elevation(size):
    xpix, ypix = size
    elevation = np.array([])
    noise = PerlinNoise(octaves=1)
    elevation = np.array([[noise([i/xpix,j/ypix]) for j in range(ypix)] for i in range(xpix)])

    return elevation

def elevation_to_rgba(elevation):
    xpix, ypix = np.array(elevation).shape
    colormap = plt.cm.get_cmap('gist_earth')
    elevation = (elevation - elevation.min())/(elevation.max()-elevation.min())
    ''' You can play around with colormap to get a landscape of your preference if you want '''
    landscape = np.array([colormap(elevation[i, j])[0:3] for i in range(xpix) for j in range(ypix)]).reshape(xpix, ypix, 3)*255
    landscape = landscape.astype('uint8')
    return landscape
 

get_landscape = lambda size: elevation_to_rgba(get_elevation(size))


if __name__ == '__main__':
    size = 640, 480
    pic = elevation_to_rgba(get_elevation(size))
    plt.imshow(pic, cmap='gist_earth')
    plt.show()