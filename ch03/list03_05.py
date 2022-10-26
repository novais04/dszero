'''
SEJA CRITERIOSO PARA USAR O plt.axis
'''
from matplotlib import pyplot as plt

mentions = [500,505]
years = [2017,2018]

plt.bar(years, mentions,0.8) 
plt.xticks(years)
plt.ylabel("of time I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5,2018.5,0,550])
plt.title("Not So Huge Anumore")
plt.savefig(r"..//dszero/ch03/figura03_05.png")
plt.show()






