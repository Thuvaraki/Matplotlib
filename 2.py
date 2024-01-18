import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# resize the plot
# plt.figure function  is used to create a new figure or adjust the properties of an existing figure
#  figure will have a width of 2 inches and a height of 1.5 inches.
# figure will have a resolution of 300 dots per inch.
plt.figure(figsize=(5,3),dpi=100)

a= np.arange(0,4.5,0.5)
plt.plot(a,a**2, color='blue',linewidth = '2',linestyle='-',label='a^2')

x = [0,1,2,3,4]
y = [0,2,4,6,8]
plt.plot(x,y,label='2x',linewidth='2',color='red',linestyle='--',marker='.',markersize='10',markeredgecolor='purple')

plt.title('My first plot',fontdict={'fontname':'Comic sans MS','fontsize':20})
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()

# to save the plot
plt.savefig('my plot',dpi=100)

plt.show()