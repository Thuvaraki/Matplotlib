import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

fifa = pd.read_csv('fifa_data.csv')
bins = [40,50,60,70,80,90]
plt.xticks(bins)

plt.title('Distribution of player skills in Fifa 2018')
plt.xlabel('skill level')
plt.ylabel('Number Of Players')

plt.hist(fifa.Overall,color='#abcdef')
plt.show()