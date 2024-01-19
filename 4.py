import matplotlib.pyplot as plt
import pandas as pd

gas = pd.read_csv("gas_prices.csv")

plt.figure(figsize=(8,5))
plt.title('Gas Prices over Time (in USD)',fontdict={'fontweight':'bold','fontsize':'18'})


plt.plot(gas.Year, gas.USA,'b.-',label='USA')
plt.plot(gas.Year, gas.Canada,'r.-',label='Canada')
plt.plot(gas.Year, gas['South Korea'],'g.-',label='South Korea')

# adding 2011 to the Year(x axis)
plt.xticks(gas.Year[::3].tolist()+[2011])
plt.xlabel('Year')
plt.ylabel('US Dollars')
plt.legend()
# plt.savefig('Gas_Price_Figure.png',dpi=100)
plt.show()

