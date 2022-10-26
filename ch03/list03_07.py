#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 07:34:51 2022

@author: anselmo

Data Science do Zero
Ch03 - Visualização

Gráficos de dispersão

Obs: O gráfico de dispersão é a opção certa para representar 
as relaçoes entre pares de conjuntos de dados
"""
import matplotlib.pyplot as plt

friends = [ 70,  65,  72,  63,  71,  64,  60,  64,  67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# construindo o gráfico
plt.scatter(friends,minutes)

# criando rótulo para cada ponto
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label, 
                 xy=(friend_count, minute_count),       # coloque o rótulo no respectivo ponto 
                 xytext=(5,-5),                         # mas levemnte deslocado
                 textcoords='offset points') 
plt.title('Daily Minutes vs Number of Friends')
plt.xlabel('# of Friends')
plt.ylabel('Daily minutes spent on the site')     
plt.savefig(r"../dszero/ch03/figura03_07.png")      
plt.show()