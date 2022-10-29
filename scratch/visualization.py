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
plt.savefig('..//ch03/figura03_01.png')
plt.show()



movies = ["Anniel Hall", "Ben-Hur","Casablanca", "Gandhi", "West Side Story"]

num_oscars = [5,11,3,8,10]

# plote as barras com coordenadas x à esquerda [0, 1, 2, 3, 4], alturas [num_oscars]

plt.bar(range(len(movies)), num_oscars)
plt.title("My favorite movis") # adiciona o título
plt.ylabel("Of Academy Awards") # adiciona rotulo do eixo y

# rotulando x com os nomes dos filmes nos centro das barras
plt.xticks(range(len(movies)),movies)
plt.savefig('..//ch03/figura03_02.png')
plt.show()


from collections import Counter

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
histogram = Counter(min(grade // 10*10,90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()], # move as barras para direita em 5
    histogram.values(), # atribui a altura correta para cada barra
    10, # Atrinui a larrgura a cada barra
    edgecolor=(0,0,0)) # escurece as bordas das barras
plt.axis([-5,105,0,5]) # eixo x de -5 a 105
# eixo y de 0 a 5
plt.xticks([10 * i for i in range(11)]) # rótulos do eixo x em 0, 10,..,100
plt.xlabel('Decile')
plt.ylabel('# of Students')
plt.title('Distribution of Exam 1 grades')
plt.savefig("..//ch03/figura03_03.png")
plt.show()


mentions = [500,505]
years = [2017,2018]

plt.bar(years, mentions,0.8) 
plt.xticks(years)
plt.ylabel("of time I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5,2018.5,499,506])
plt.title("Look at the 'Huge' Increase!")
plt.savefig(r"../ch03/figura03_04.png")
plt.show()

mentions = [500,505]
years = [2017,2018]

plt.bar(years, mentions,0.8) 
plt.xticks(years)
plt.ylabel("of time I heard someone say 'data science'")
plt.ticklabel_format(useOffset=False)
plt.axis([2016.5,2018.5,0,550])
plt.title("Not So Huge Anumore")
plt.savefig(r"../ch03/figura03_05.png")
plt.show()

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
plt.savefig("..//ch03/figura03_06.png")
plt.show()

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
plt.savefig(r"../ch03/figura03_07.png")      
plt.show()

test_1_grades = [99,90,85,97,80]
test_2_grades = [100,85,60,90,70]
labels = ['a','b','c','d','e']

plt.scatter(test_1_grades, test_2_grades)
for label, test1_count, test2_count in zip(labels, test_1_grades, test_2_grades):
    plt.annotate(label, 
                 xy=(test1_count, test2_count),  # coloque o rótulo no respectivo ponto 
                 xytext=(5,-5),                  # mas levemnte deslocado
                 textcoords='offset points') 
plt.title("Axes Aren't Comparable")
plt.xlabel("Test 1 grade")
plt.ylabel("test_2_grade")
plt.savefig(r"../ch03/figura03_08.png")           
plt.show()



plt.scatter(test_1_grades, test_2_grades)
for label, test1_count, test2_count in zip(labels, test_1_grades, test_2_grades):
    plt.annotate(label, 
                 xy=(test1_count, test2_count),  # coloque o rótulo no respectivo ponto 
                 xytext=(5,-5),                  # mas levemnte deslocado
                 textcoords='offset points') 
plt.axis("equal")
plt.title("Axes Comparable")
plt.xlabel("Test 1 grade")
plt.ylabel("test_2_grade")
plt.savefig(r"..ch03/figura03_09.png")           
plt.show()


