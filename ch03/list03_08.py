#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 07:34:51 2022

@author: anselmo

Data Science do Zero
Ch03 - Visualização

Gráficos de dispersão

Obs: Se deixarmos que o matplotlib selecione a escla ao dispersar 
as variáveis comparáveis, talvez você obtenha um imagem equivocada 
"""
import matplotlib.pyplot as plt

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
plt.savefig(r"../dszero/ch03/figura03_08.png")           
plt.show()