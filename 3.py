import matplotlib.pyplot as plt

labels = ['A','B','C']
values = [1,2,4]

plt.figure(figsize=(6,4))

bars = plt.bar(labels,values)

# bars[0].set_hatch('/')
# bars[1].set_hatch('-')
# bars[2].set_hatch('*')

patterns = ['/','-','*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.show()