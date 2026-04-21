# si coloco el valor cero, me muestra a que letra corresponde.
miTexto = "Esto es una pequeña prueba"
resultado = miTexto[0]
print(resultado)

# Uso del método index / en este caso me muesrta la posición donde
# se encuentra la letra r
miNueboTexto = "tengo otro ejemplo"
print(miNueboTexto.index('r'))

# Buscar desde un índice
miNuevoTexto = "esta junto a tengo otro Ejemplo"
print(miNuevoTexto.index('a',0)) # comienza a buscar desde el índice 0 hacia adelante

print(miNuevoTexto.index('a',5)) # comienza a buscar desde el índice 5 adelante

# Otro ejemplo inclyuendo substring, start y end
frase = "esta noche voy a escribir los versos más tristes que nunca eh escrito"
print(frase.index('o',3,12)) # me toma la letra o, empieza de 3 y salta de doce en doce

# Búsqueda inversa
print(frase.rindex('a')) # me busca de izquierda a derecha y me muestra la posición

palabra = "ordenador"
print(palabra.index('a'))
