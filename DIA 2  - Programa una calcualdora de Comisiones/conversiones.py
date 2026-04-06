# Conversiones implícitas
num1 = 20
num2 = 30.5


num1 = num1 + num2 
# en este caso num1 lo sumo con num2 y python lo comvierte implícitamente en float

print(type(num1))
print(type(num2))

# conversiones explícitas
num3 = 5.8
print(num3)
print(type(num3))

# ahora hacemos la conversión
num_entero = int(num3)
print(type(num_entero))

# otro ejemplo
edad = input("Coloca tu edad: ")

print(type(edad))

edad = int(edad)

nueva_edad = edad + 1

print(nueva_edad)