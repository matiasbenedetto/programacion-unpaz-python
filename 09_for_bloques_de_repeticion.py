# FOR: BLOQUES DE REPETICIÒN

# Cuando queremos repetir bloques de còdigo una cantidad determinada de veces podemos hacer uso de los bucles for.
# For se utiliza en conjunto con una objeto iterable, es decir, un objeto que se puede recorrer como una secuencia


# Ejemplo 1. Se imprimen en pantalla numeros del 0 al 11
for numero in range(12):
    print (numero)


# Ejemplo 2. Se imprimen en pantalla numeros del 100 al 150
for num in range(100,151):
    print (num)


# Ejemplo 3. Se imprime cada caracter de un string
mi_variable_string = "Hola yo soy un texto guardado en una variable de cadena de caracteres (string)"
for caracter in mi_variable_string:
    print (caracter)


# Ejemplo 6. Se imprime cada elemento de una lista de numeros enteros
edades = [18, 24, 33, 40, 38, 22, 26, 51, 44]
for edad in edades:
    print (edad)


# Ejemplo 5. Se imprime cada elemento de una lista de strings
nombres = ["Juana", "Alberto", "Lucia", "Daniela", "Carlos", "Federico"] 
for nombre in nombres:
    print(nombre)

