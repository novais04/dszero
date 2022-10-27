
'''
ESTATISTICA

Colocando as contagens de amigos em um histograma usando
Counter e plt.bar
'''
from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friends_counts = Counter(num_friends)
xs = range(101) # omaior valor é 100
ys = [friends_counts[x] for x in xs] # a altura indicao n° de amigos
plt.bar(xs,ys)
plt.axis([0,101,0,25])
plt.title("histograma de contagem de amigos")
plt.xlabel("n° de Amigos")
plt.ylabel("# of people")
# plt.savefig("..//ch05/figura05_01;png")
plt.show()