import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Basic graph
x = [0,1,2,3,4]
y = [0,2,4,6,8]

plt.plot(x,y, label='2x', color='red',linewidth = '2',linestyle='--', marker='.',markersize='10',markeredgecolor='purple')

# short hand notation
# fmt= '[color][marker][line]'
# plt.plot(x,y, 'r.--', label='2x')

plt.title('My first plot',fontdict={'fontname':'Comic sans MS','fontsize':20})
plt.xlabel('x label')
plt.ylabel('y label')
plt.xticks([0, 2,4]) # Specify the x-axis tick positions
plt.legend() #to display labels
plt.show()