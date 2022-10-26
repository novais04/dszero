''''
Gráficos de Barras

Exemplo:
Número de Oscars recebiso pelos filmes indicados
'''

import matplotlib.pyplot as plt

movies = ["Anniel Hall", "Ben-Hur","Casablanca", "Gandhi", "West Side Story"]

num_oscars = [5,11,3,8,10]

# plote as barras com coordenadas x à esquerda [0, 1, 2, 3, 4], alturas [num_oscars]

plt.bar(range(len(movies)), num_oscars)
plt.title("My favorite movis") # adiciona o título
plt.ylabel("Of Academy Awards") # adiciona rotulo do eixo y

# rotulando x com os nomes dos filmes nos centro das barras
plt.xticks(range(len(movies)),movies)
plt.savefig('..//dszero/ch03/figura03_02.png')
plt.show()
  