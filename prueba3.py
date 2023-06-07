#Suma de elementos de una lista: Escribe un programa que sume todos los elementos de una lista dada.
from functools import reduce
lista = [2, 4, 6, 8]
suma = reduce(lambda x, y: x + y, lista )
print(suma) 