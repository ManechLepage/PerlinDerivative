import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cbook, cm
from matplotlib.colors import LightSource

import heightGenerator

fig = plt.figure()
ax = plt.axes(projection='3d')

size = (256, 256)

x = np.linspace(round(-size[0] / 2), round(size[0]), size[0])
y = np.linspace(round(-size[1] / 2), round(size[1]), size[1])
x, y = np.meshgrid(x, y)


z = np.array(heightGenerator.initialize_grid(size))

ls = LightSource(270, 45)

rgb = ls.shade(z, cmap=cm.gist_earth, vert_exag=0.1, blend_mode='soft')
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
                       linewidth=0, antialiased=False, shade=False)

ax.set_zlim(-2.5, 2.5)

plt.show()
