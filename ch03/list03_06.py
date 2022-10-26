#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 07:34:51 2022

@author: anselmo

Data Science do Zero
Ch03 - Visualização

Gráficos de linhas

plt.plot

"""
import matplotlib.pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared = [256, 128, 64,32, 16,8,4,2,1]

total_error = [x+ y for x,y in zip(variance, bias_squared)] 
xs = [i for i, _ in enumerate(variance)]

# podemos fazer multiplas chamadas para plt.plot
# para mostrar múltiplas sérires no mesmo gráfico

plt.plot(xs, variance, 'g-', label='variance') # linha verde sólida
plt.plot(xs,bias_squared, 'b:', label='Bias²' ) # linha vermelha de ponto 
                                                # tracejado
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The bias-Variance Tradeoff")
plt.savefig("..//dszero/ch03/figura03_06.png")
plt.show()