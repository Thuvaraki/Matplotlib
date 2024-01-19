import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv("fifa_data.csv")

plt.style.use('default')

barcelona = fifa.loc[fifa['Club'] == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa['Club'] == 'Real Madrid']['Overall']

labels = ['FC Barcelona','Real Madrid']

bp = plt.boxplot([barcelona,madrid],labels=labels,patch_artist = True,medianprops={'linewidth': 2,'color':'red'})

plt.title('Professional Soccer Team Comparison')
plt.ylabel('FIFA Overall Rating')

for box in bp['boxes']:
    box.set(color = '#4286f4',linewidth = 2)
    box.set(facecolor = '#e0e0e0')
    # change hatch
    # box.set(hatch = '/')

plt.show()
