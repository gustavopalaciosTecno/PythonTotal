"""
¿Qué es una variable?
Imagina que tienes una caja donde guardas algo. 
Le pones una etiqueta para saber qué hay adentro. 
Eso es exactamente una variable: un nombre que apunta a un valor.
"""
# Ejemplo de variables
nombre = "Néstor Gustavo"
print(nombre)

# para saber que tipo de datos maneja mi variable, agregar la función type
print(type(nombre))

# tipo de dato entero
numero = 44
print(type(numero))


# tipo de dato flotante
sueldo = 1325.44
print(type(sueldo))

# tipo de dato lista
apellidosEspañoles = ["Gonzalez","Fernandez","Marquez","Vazquez"]
print(type(apellidosEspañoles))

# tipo de dato diccionario
miDiccionario = {
    1:'María',
    2:'Leopolda',
    3:'Manuela',
    4:'Ricarda'
}

print(type(miDiccionario))

# Tipo de dato conjunto
conjuntoColores = {'verde','amarillo','azul','marrón','violeta'}
print(type(conjuntoColores))

# tipo de dato Booleano
verdadero = True
falso = False
print(type(verdadero),type(falso))