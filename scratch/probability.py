#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:52:55 2022

@author: anselmo

Probabilidade
"""

# DISTRIBUIÇÃO CONTINUA

def uniform_cdf(x: float)-> float:
    "Retorna  a probabilidade de uma variável aleatória uniforme ser < = x"
    if x < 0:
        return 0 # a aleatória uniforme nunca será menor que 0
    elif x < 1:
        return x # ex P(x ,= 0.4) = 0.4
    else:
        return 1 # a aleatória uniforme semre é menor do que 1

# DISTRIBUIÇÃO NORMAL

import matplotlib.pyplot as plt
import math

SQRT_TWO_PI =math.sqrt(2 * math.pi)

def normal_pdf(x:float, mu:float = 0, sigma: float =1) -> float:
    return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))

# platagem de alguma PDFs para confeir o visual

xs = [x / 10.0 for x in range(-50,50)]

plt.plot(xs, 
        [normal_pdf(x, sigma =1) for x in xs],
        '-', 
        label= "mu=0, sifma=1")

plt.plot(xs,
         [normal_pdf(x, sigma=2) for x in xs],
         '--',
         label = "mu=0, sigma=2")

plt.plot(xs,
         [normal_pdf(x, sigma = 0.5) for x in xs],
         ':',
         label= "mu=u, sigma = 0.5")

plt.plot(xs,
         [normal_pdf(x, mu=-1) for x in xs],
         '-.',
         label = "mu=-1, sigma=1")
plt.legend(loc=1)
plt.title("Various Normal pdfs")
#plt.savefig("..//img/figura06_02.png")
plt.show()

# DISTRIBUIÇÃO NORMAL PADRÃO

def normal_cdf(x:float, mu:float=0, sigma: float = 1 )-> float:
    return (1 + math.erf((x-mu) / math.sqrt(2) / sigma)) / 2

# Plotando algumas CDFs de exemplo

xs = [x / 10.0 for x in range(-50,50)]

plt.plot(xs,
         [normal_cdf(x,sigma =1) for x in xs],
         "-",
         label = "mu=o, sigma = 1")
plt.plot(xs,
         [normal_cdf(x, sigma=2) for x in xs],
         "--",
         label="mu=0, sigma = 2")
plt.plot(xs,
         [normal_cdf(x, sigma =0.5) for x in xs],
         ":",
         label = "mu=0, sigma = 0.5")
plt.plot(xs,
         [normal_cdf(x, mu =-1)for x in xs],
         "-.",
         label = "mu=-1, sigma =1")
plt.legend(loc=4) # no canto direito
plt.title("Various Normal cdfs")
#plt.savefig("..//img/figura06_03.png")
plt.show()

# Pesquisa binária
def inverse_normal_cdf(p:float, mu:float = 0, sigma:float=1, tolerance:float=0.00001)->float:
    """Encontre o inverso aproximado unsadno a pesquisa binária"""
    # se não for padrão, compute o padrão e redimensione
    if mu != 0 or sigma!= 1:
        return mu + sigma * inverse_normal_cdf(p,tolerance=tolerance)
    
    low_z = -10.0 # normal_cdf(-10) = é (muito próximo de ) 0
    hi_z = 10.0 # normal_cdf(10) é (muito próximo de ) 1
    
    while hi_z > tolerance:
        mid_z = (low_z + hi_z) /2 # cosidere o ponto médio 
        mid_p = normal_cdf(mid_z) # é valor de cdf
        
        if mid_p < p:
            low_z = mid_z # ponto médio é muito baixo, procure um maior
        else:
            hi_z = mid_z # ponto médio é muito alto, procure um menor
    return mid_z        

# O TEOREMA DE LIMITE CENTRAL
import random

def bernoulli_trial(p:float) -> float:
    """Retorna 1 com probabilidade p e 0 com a probabilidade 1-p"""
    return 1 if random.random() < p else 0

def binominal(n:int, p:float)-> int:
    """retorna a soma de n trials bernoulli(p)"""
    return sum(bernoulli_trial(p) for _ in range(n))

# plotando um demostração

from collections import Counter
def binominal_histogram(p:float, n:int, mum_points:int)-> None:
    """seleciona pontos de uma binominal(n,p) e plota se histograma"""
    data = [binominal(n,p) for _ in range(num_points)]
    histogram = Counter(data)
    
    plt.bar([x - 0.4 for x in histogram.key()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')
    mu = p * n
    sigma = math.sqrt(n*p(1-p))  
    
    #use um gráfico de linhas para indicar a aproximação normal
    
    xs = range(min(data), mas(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma) for x in xs]
    
    plt.plot(xs,ys)
    plt.title("Biniminal distribuition vs. normal distribuition")                                                  
    
    plt.show()



#***********************************************************************#
def main():
    import enum, random

    """Um enum é um conjunto tipado de valores enumerados que 
    deixa # o código mais descritivo e legível"""



    class Kid(enum.Enum):
        BOY = 0
        GIRL = 1
        
    def random_kid()-> Kid:
        return random.choice([Kid.BOY, Kid.GIRL])
    
    both_girls = 0
    older_girl = 0
    either_girl = 0
    
    random.seed(0)
    
    for _ in range(1000):
        younger = random_kid()
        older = random_kid()
        if older == Kid.GIRL:
            older_girl += 1
        if older == Kid.GIRL and younger == Kid.GIRL:
            both_girls += 1
        if older == Kid.GIRL or younger == Kid.GIRL:
            either_girl +=1
            
   # print("P(both|older):", both_girls / older_girl)# 0,514 ~1/2
   # print("P(both|either):", both_girls / either_girl) # 0.342 ~ 1/3
    
    assert 0.48 < both_girls / older_girl < 0.52
    assert 0.30 < both_girls / either_girl < 0.35
    
if __name__ == "__main__": main()