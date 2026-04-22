"""
Aplicamos distintas formas para fragmentar (slicing) los textos
"""

# los carcateres del índice empieza desde el 1
abcedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(abcedario[7:12]) # excluye 7 carcateres hasta el valor 12
print(abcedario[3:6]) # excluye 3 carcateres hasta el valor 6
print(abcedario[5:8]) # excluye 5 carcateres hasta el valor 8
print(abcedario[0:10]) # incluye desde el primero hasta el 10


print(abcedario[0:10:2]) # incluye desde el primero hasta el 10 de dos en dos hasta completar la cantida asignada

print(abcedario[0:15:2]) # empieza de cero, toma 15 valores y va de dos en dos hasta completar la cantida asignada

# Me imprime las letas de derecha a izquierda
print(abcedario[::-1]) # me incluye todos, va de cero en uno en uno (-1)y al tener signo menos (-1) comienza de la última letra