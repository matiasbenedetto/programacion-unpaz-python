# LISTAS
# Las listas en Python son un tipo de estructura de dato que se utiliza para almacenar varios valores dentro de ellas.
# Nos otorgan varias facilidades a la hora de guardar y acceder series de datos no serian posibles con los tipos de variables básicos que ya vimos (int, float, string, boolean)

# DEFINIR LISTAS

# Definición de una lista vacia
milista = []

# Definición de una lista de ints (numeros enteros)
cantidades = [23, 44, 88, 109, 215, 62, 99, 4, 51, 8]

# Definicion de una lista de strings (cadenas de caracteres)
nombres = ["Pedro", "Carla", "Marina"]

# Definición de una lista de booleans
respuestas = [True, False, False, False, True, False]


# ACCEDER A ELEMENTOS DE UNA LISTA POR SU INDICE
# Para acceder a un elemento de una lista podemos inidicar el nombre de la lista y entre corchetes el numero de elemento (índice) al que queremos acceder.
# Recorda que siempre se comienza a contar desde cero. El primer elemento es el 0 y el segundo el 1

# Imprimimos el cuarto elemento de lista cantidades
print ( cantidades[3] )

# Imprimimos el segundo elemento de la lista cantidades
print ( cantidades[1] )

# Imprimimos el tercer elemento de la lista de nombres
print ( nombres[2] )

# Imprimimos el quinto elemento de la lista de respuestas
print (respuestas[4] )