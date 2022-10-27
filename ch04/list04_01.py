#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Álgebra Linear
Created on Wed Oct 26 11:01:40 2022

@author: anselmo
Vetores

exemplo de vetor sendo um lista de float
"""

from typing import List


Vector = List[float]

height_weight_age = [70,    # polegadas 
                     170,   # libras
                     40]    # anos

grades = [95,   # teste1
          80,   # teste2
          75,   # teste3
          62]   # teste4

def add(v:Vector, w:Vector)-> Vector:
    '''Soma os elementos correspondentes'''
    assert len(v) ==len(w), "vetor deve ser do mesmo tamanho"
    return [v_i + w_i for v_i,w_i in zip(v,w)]

assert add([1,2,3],[4,5,6])== [5,7,9]

'''
Da mesma forma para subtrair dois vetores basta
subtrair os elementos correspondentes
'''
def subtract(v:Vector, w: Vector)-> Vector:
    '''Subtrai os elementos correspondentes'''
    assert len(v) ==len(w), "vetores devem ser do mesmo tamanho"
    return [v_i - w_i for v_i,w_i in zip(v,w)]

assert subtract([5,7,9],[4,5,6]) == [1,2,3]

'''
às vezes é ecessário somar uma lista de vetors por componete
'''
def vector_sum(vectors: List[Vector])-> Vector:
    ''' soma todos os elementos correspondentes'''
    # verifique se os vetores estão vazios
    assert vectors, "no vectors provided"
    
    #verifica se os vetorres são do mesmo tamanho
    num_elements = len(vectors[0])
    
    assert all(len(v)== num_elements for v in vectors), "tamanho diferente!"
    
    # o elemento de n°i do resultado éa soma de todo Vector[i]
    return [sum(Vector[i] for Vector in vectors) for i in range(num_elements)]

assert vector_sum([[1,2,],[3,4],[5,6], [7,8]]) == [16,20]
    
'''
multiplicando vetor
''' 
def scalar_multiply(c:float,v: Vector)-> Vector:
    ''' multiplica cada elemento por c'''
    return [c*v_i for v_i in v]

assert scalar_multiply(2,[1,2,3]) == [2,4,6]

'''
Média dos componentes de uma lista
'''
def vector_mean(vectors: List[Vector]) -> Vector:
    '''Computa a média dos elementos'''
    n = len(vectors)
    
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1,2],[3,4],[5,6]]) == [3,4]
    
'''
produto scalar
'''
def dot(v:Vector, w:Vector)-> float:
    '''Computa v_1+..+v_n*w_n'''
    assert len(v) == len(w), " vetor deve ser do mesmo tamanho"
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

assert dot([1,2,3], [4,5,6]) == 32 # 1*4 + 2*5 + 3 * 6   
 

# Computando a soma dos quadrados


def sum_of_squares(v:Vector)-> float:
    '''retorna v_1+...+v_n*v_n'''
    return dot(v,v)

assert sum_of_squares([1,2,3]) == 14 # 1*1 + 2*2 + 3*3

'''
Computando a magnitude
'''
import math 

def magnitude(v:Vector)-> float:
    ''' retorna a magnitude(ou comprimento) de v'''
    return math.sqrt(sum_of_squares(v))# math.sqrt é a função de 
                                        #raiz quadrada
assert magnitude([3,4]) == 5
                     