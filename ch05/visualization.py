#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 08:06:58 2022

@author: anselmo
"""
from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]

gdp = [300.2,543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# criando um grafico de linhas, anos no eixo x, gdp no eixo y
plt.plot(years,gdp, color='green', marker='o',linestyle='solid')

# adicione um título 
plt.title("Nominal GDP")
#adicone oum rótulo ao eixo y
plt.ylabel('Billions of $')
plt.xlabel('Year')
plt.savefig('..//dszero/ch03/figura03_01.png')
plt.show()
