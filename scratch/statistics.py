#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 08:33:09 2022

@author: anselmo
"""


# ESTATISTICA

# Colocando as contagens de amigos em um histograma usando
# Counter e plt.bar

import matplotlib.pyplot as plt
from typing import List
from collections import Counter

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,
               13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,
               10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,
               8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,
               6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,
               4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,
               3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friends_counts = Counter(num_friends)
xs = range(101) # omaior valor é 100
ys = [friends_counts[x] for x in xs] # a altura indicao n° de amigos
plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.title("histograma de contagem de amigos")
plt.xlabel("n° de Amigos")
plt.ylabel("# of people")
plt.savefig("..//ch05/figura05_01;png")
plt.show()


num_points = len(num_friends) # 204

# consultando os valores mais altos e mais baixos
largest_value = max(num_friends) # 100
smallest_value = min(num_friends) # 1

#constuladno um valor de um posição específica 
sorted_values = sorted(num_friends) # criando uma nova lista ordenaa
smallest_value = sorted_values[0] # 1
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2] # 49

assert smallest_value == 1
assert second_smallest_value == 1
assert second_largest_value == 49

#print(f'Lista sem ordenação:\n {num_friends}')
#print(f'\nLista Ordenada:\n{sorted_values}\n')
#print(f'Maior valor: {largest_value} - Menor valor: {smallest_value}')
#print(f"\nvalor da posição [0]: {smallest_value}")
#print(f'\nSegundo menor valor: {second_smallest_value } - Segundo maior valor: {second_largest_value}')

#****************************************************************#

# ESTATISTICA

# Tendências Centrais


# Média
def mean(xs:List[float])-> float:
    return sum(xs)/len(xs)

# print(mean(num_friends)) # 7.333

assert 7.3333 < mean(num_friends) < 7.3334

# mediana
# Sunlinhado indica que esta função é privada
# dev ser chamdas pela função mediana, mas não por outro usuário
# da biblioteca estatística

def _median_odd(xs:List[float])-> float:
    """Se len(xs) for impar, a mediana será o elemento do meio"""
    return sorted(xs)[len(xs)//2]

def _median_even(xs:List[float])-> float:
    """se len(xs) for par, ela será a média dos dosis elementos do meio"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs)//2 #comprimento 4 -> hi_midpoint = 2
    return (sorted_xs[hi_midpoint-1]+sorted_xs[hi_midpoint]) / 2

def median(v:List[float])-> float:
    """ encontra o valor do meio de v"""
    return _median_even(v) if len(v)%2 ==0 else _median_odd(v)

# print(median([1,10,2,9,5])) # 5
# print(median([1,9,2,10]))     # 5,5 

assert median([1,10,2,9,5]) == 5
assert median([1,9,2,10]) == (2+9)/2

# computando a mediana do número de amigos 
#print(f"Média da lista num_frinds: {median(num_friends)}") # 6

# quartil

def quantile(xs:List[float], p:float)-> float:
    """ Retorna o valor pth-percentile em x"""
    p_index = int (p * len(xs))
    
    return sorted(xs)[p_index]

#print(f"0.10 -> {quantile(num_friends,0.10)}")  # 1
#print(f"0.25 -> {quantile(num_friends,0.25)}")  # 3
#print(f"0.75 -> {quantile(num_friends,0.75)}")  # 9
#print(f"0.90 -> {quantile(num_friends,0.90)}")  # 13


assert quantile(num_friends,0.10) ==  1
assert quantile(num_friends,0.25) ==  3
assert quantile(num_friends,0.75) ==  9
assert quantile(num_friends,0.90) ==  13

# moda

def mode(x:List[float])-> List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]

#print(mode(num_friends))

assert set(mode(num_friends)) == {1,6}

#*************************************************************************#

# Dispersão
# Amplitude - diferença entre a maior e menor amostra
def data_range(x:List[float])->float:
    return max(x)-min(x)

# print(data_range(num_friends))  # 99
assert data_range(num_friends) == 99

# VARIÂNCIA 

from linear_algebra import sum_of_squares

def de_mean(xs:List[float])-> list[float]:
    """desloca x ao subtrair sua média (então o resultado tem a média 0)"""
    x_bar = mean(xs)
    
    return [x -x_bar for x in xs]

def variance(xs:List[float])->float:
    """presume que x tem ao menos dois elementos"""
    assert len(xs) >= 2 , "variancia requer média da média"
    n = len(xs)
    desviations = de_mean(xs)
    
    return sum_of_squares(desviations) / (n -1)

# print(f"Variancia: {variance(num_friends)}")

assert 81.54 < variance(num_friends)< 81.55    

#calculando o dessvio padrão

import math

def standard_deviation(xs:List[float])-> float:
    """O desvio padrão éa a raiz quadrada da variância"""
    return math.sqrt(variance(xs))

# print(f"Descio-Padrão: {standard_deviation(num_friends)}")
assert 9.02 < standard_deviation(num_friends) < 9.04

"""
computa a diferença entre os percentos (quantos)
75% e 25% do valor
"""

def interquantile_range(xs:List[float])-> float:
    """Retorna a diferença entre o percentil 75% e o percentil 25%"""
    return quantile(xs,0.75) - quantile(xs, 0.25)

# print(interquantile_range(num_friends)) # 6
assert interquantile_range(num_friends) == 6

# CORRELAÇÃO

"""
A vice-presidente de Crescimento na DataSciencester tem uma teoria que a
quantidade de tempo gasto pelas pessoas no site é relacionada ao número de
amigos que elas possuem (ela não é uma vice-presidente à toa), e ela pediu para
você verificar isso.

Após examinar os registros do tráfego, você desenvolve uma lista daily_minutes que
mostra quantos minutos por dia cada usuário passa na DataSciencester e você
havia ordenado essa lista para que seus elementos correspondessem aos
elementos da lista anterior num_ friends . Gostaríamos de investigar a relação entre
essas duas métricas.
"""
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,
                 54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,
                 35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45
                 ,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,
                 32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,
                 36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,
                 36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,
                 35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,
                 24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,
                 35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,
                 35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,
                 27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,
                 18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,
                 29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,
                 37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,
                 25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,
                 20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,
                 31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,
                 14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,
                 31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

daily_hours = [dm / 60 for dm in daily_minutes]

# Primeiro, investigaremos a covariância, o equivalente pareado da variância.
# Enquanto a variância mede como uma única variável desvia de sua média, a
# covariância mede como duas variáveis variam em conjunto de suas médias:

from linear_algebra import dot 
    
def covariance(xs:List[float], ys: List[float])-> float:
    assert len(xs) == len(ys), "xs e ys devem ter o mesmo número de elementontos"
    return dot(de_mean(xs), de_mean(ys))/(len(xs)-1)

#print(covariance(num_friends, daily_minutes))
#print(covariance(num_friends, daily_hours))

assert 22.42 < covariance(num_friends, daily_minutes) < 22.43
assert 22.42/60 < covariance(num_friends, daily_hours) < 22.43/60

def correlation(xs:List[float],ys:List[float])-> float:
    "mede a variação simutânea de xs e ys a partir das sua médias"
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys) 
    if stdev_x > 0 and stdev_y > 0:
        return covariance(xs,ys) / stdev_x / stdev_y
    else:
        return 0 # se não houver cariação,  a correlação é zero
# print(correlation(num_friends, daily_minutes))
# print(correlation(num_friends, daily_hours))

assert 0.24 < correlation(num_friends, daily_minutes) < 0.25
assert 0.24 < correlation(num_friends, daily_hours) < 0.25


# ingnorando o outlier
outlier = num_friends.index(100) # índice do outlier
num_friends_good = [x for i,x in enumerate(num_friends) if i != outlier]

daily_minutes_good = [x for i,x in enumerate(daily_minutes) if i != outlier]
daily_hours_good = [dm / 60 for dm in daily_minutes_good]

#print(correlation(num_friends_good, daily_minutes_good))
#print(correlation(num_friends_good, daily_hours_good))

assert 0.57 < correlation(num_friends_good, daily_minutes_good) < 0.58
assert 0.57 < correlation(num_friends_good, daily_hours_good) < 0.58


# obtenha a lista de tuplas de duas listas
# e mescle-as usando zip().
lista_tuplas = list(zip(num_friends_good, daily_minutes_good))

"""
Você averígua e descobre que o valor discrepante era, na verdade, uma conta
teste interna que ninguém se preocupou em remover. Então sinta-se bem ao
excluí-la.
"""

#**************************************************************************#
# PARADOXO DE SIMPSON

"""
Uma surpresa incomum ao analisar dados é o Paradoxo de Simpson, em que as
correlações podem ser enganosas quando as variáveis de confusão são ignoradas.
"""
