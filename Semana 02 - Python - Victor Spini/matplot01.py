import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plt.plot([1, 2, 3], [2, 4, 6])

# x = [1, 2, 3]
# y = [2, 4, 6]

x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

# Resize Graph
plt.figure(figsize=(5, 3), dpi=100)

# Line Number One
# Keyword Argument Notation
plt.plot(x,
         y,
         label='2x',
         color='green',
         linewidth=2,
         marker='.',
         linestyle='--',
         markersize=15,
         markeredgecolor='blue')

# Shorthand notation
# fmt = '[color][marker][line]'
# plt.plot(x,y, 'b^--', label='2x')

# Line Number two
# Select interval to plot point at
x2 = np.arange(0, 4.5, 0.5)

# plt.plot(x2, x2**2, 'r', label='x²')

# Plot part of the graph as Line
plt.plot(x2[:5], x2[:5]**2, 'r', label='x²')

# Plot raminder of  graph as a dot
plt.plot(x2[4:], x2[4:]**2, 'r--')

# Add a title (specify font parameters with fontdict)
plt.title('First Graph!',
          fontdict={
              'fontname': 'Comic Sans MS',
              'fontsize': 20
          })

# x and y Labels
plt.xlabel('x Axis')
plt.ylabel('y Axis')
# plt.xlabel('x Axis', fontdict={'fontname': 'Comic Sans MS'})
# plt.ylabel('y Axis', fontdict={'fontname': 'Comic Sans MS'})

# x, y axis Tickmarks (scale of graph)
plt.xticks([0, 1, 2, 3, 4])
# plt.yticks([0, 2, 4, 6, 8, 10])

# Add a legend
plt.legend()
# Save figure (dpi 300 is good when saving so graph has high resolution)
# plt.savefig('graph.png', dpi=300)

# Show plot
plt.show()
