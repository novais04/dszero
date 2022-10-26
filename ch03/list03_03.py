''''
Representando histogramas

'''

import matplotlib.pyplot as plt
from collections import Counter

from sqlalchemy import values

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
plt.savefig("..//dszero/ch03/figura03_03.png")
plt.show()
