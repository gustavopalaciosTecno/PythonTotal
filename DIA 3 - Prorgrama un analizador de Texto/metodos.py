"""
En python existen varios métodos, algunos de ellos son:
Upper() significa pasar a mayúsculas
Lower() sigfniica pasar a minúsculas
Split() significa separar en partes(listas)
Join() signfica unir items usando separador
find() encontrar un sub-string    
replace() reemplazar un sub-string
"""

# Uso de upper()
nombre = "nestor gustavo palacios meyer"
print(nombre.upper())

# Uso de lower()
apellidos = "ZANABRIA"
print(apellidos.lower())

# Uso de split()
datos = "me gusta programar en python"
print(datos.split()) # me separa las palabras en una lista

frase = "ojo al piojo, dijo Orozco, el cojo"
print(frase.split('o')) # me excluye la letra o en la frase

# Uso de join()
a = "Aprender"
b ="Python"
c ="es"
d = "Genial"
e = " ".join([a,b,c,d])
print(e)

# Uso de find()
pelicula = "lo que el viento se llevó"
print(pelicula.find('viento')) # la palabra viento empieza en el índice 10


# Uso de repalce
animales = "leon, puma, tigre, hiena"
print(animales.replace(",","/")) # reemplaza la coma por el paréntesis