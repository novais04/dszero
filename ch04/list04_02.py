'''
Matriz é uma lista de listas
Letras maiúsculas-- > matrizes
Letras minísculas --> elementos
'''
from typing import List

# outro alias de tipo
Vector = List[float]
Matrix = List[List[float]]

A = [[1,2,3], # A tem duas linhas e três colunas
     [4,5,6]]
B = [[1,2], # B tem 3 linhas e 2 colunas
     [3,4],
     [5,6]]

from typing import Tuple

def shape(A:Matrix)-> Tuple[int, int]:
    '''(n� de linhas de A e o n� de colunas de A)'''
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # n�meor de elementos na primeira linha
    
    return num_rows, num_cols

#print(shape([[1,2,3],[4,5,6]]))

assert shape([[1,2,3],[4,5,6]]) == (2,3) # 2 linhas e 3 colunas

def get_row(A:Matrix, i:int)-> Vector:
    '''retorna a linha [i] de A ( como um vetor)'''
    return A[i]  # A[i] j� est� na linha i

def get_column(A:Matrix, j:int)-> Vector: 
    ''' Retorna a coluna [j] de A (como um vetor)'''
    return [A_i[j] for A_i in A] # elemento J da linha A_i para cada linha A_i


'''
Criando uma matriz
'''
from typing import Callable

def make_matrix(num_rows:int, 
                num_cols:int,
                entry_fn:Callable[[int,int],float])-> Matrix:
    '''
    Retorna uma matriz num_row x num_cols cunda entrada (i,j) é entry_fn(i,j)
    '''
    return [[entry_fn(i,j) 
             for j in range(num_cols)] 
             for i in range(num_rows)]
    
def identity_matrix(n:int) -> Matrix:
    '''retorna a matriz de indentidade n x n'''
    return make_matrix(n,n, lambda i,j:1 if i==j else 0)

#print(identity_matrix(5))

assert identity_matrix(5) == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]