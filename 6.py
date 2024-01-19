import pandas as pd
import matplotlib.pyplot as plt

fifa = pd.read_csv("fifa_data.csv")

right = fifa.loc[fifa['Preferred Foot'] =='Right'].count()[0]
left = fifa.loc[fifa['Preferred Foot'] =='Left'].count()[0]

labels = ['left','right']
colors = ['#abcdef','#aabbcc']
plt.pie([left,right],labels=labels,colors=colors,autopct='%.2f%%')
plt.title('Foot preference table of Fifa palyers')
plt.show()
