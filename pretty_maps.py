"""
Potential Dependencies:
osmnx, descartes, shapely, numpy, vsketch
"""

# In Terminal: pip install prettymaps

import prettymaps
from matplotlib import pyplot as plt

plot = prettymaps.plot(
    # Carcassonne Coordinates
    '43.206412477118896, 2.3639343079689494',
    preset = 'default'
)

plt.savefig('test.jpg')
plt.show()
