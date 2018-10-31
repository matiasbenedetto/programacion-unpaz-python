# CONDICIONES CON IF

# En Python podemos utilizar estructuras de control de flujo condicionales en este caso vemos como funciona el if
# En estos ejemplo hay que destacar el uso de la identación o sangrado


# ESTRUCTURAS CONDICIONALES COMPARANDO NÚMEROS
precio = 120

print ("Ejemplo 1:")
# Se compara el valor de la variable precio con 90 y si es mayor se imprime un mensaje en pantalla
if precio > 90:
    print ("El precio es mayo a $90")

print ("Ejemplo 2:")
# Se compara el valor de la variable con 200 y se imprime un mensaje si es mayor y otro si es menor
if precio > 200 :
    print ("El precio es mayor a $200")
else:
    print ("El precio es menor a $200")

print ("Ejemplo 3:")
# Se comprueba mas de una condicion
if precio > 300 :
    print ("El precio es mayor a $300")
elif precio > 200:
    print ("El precio es mayor a $200")
elif precio > 100:
    print ("El precio es mayor a $100")
else:
    print ("El precio es menor a $100")


# ESTRUCTURAS CONDICIONALES CON VARIABLES BOOLEANAS (VERDADERO O FALSO)
estudiante = True

print ("Ejemplo 4:")
# Estructura condicional simple, se verifica si la variable estudiante es verdadera
if estudiante:
    print ("Es estudiante")

print ("Ejemplo 5:")
# Estructura codicional doble
if estudiante:
    print ("Es estudiante")
else:
    print ("No es estudiante")


# ESTRUCTURAS CONDICIONALES CON STRINGS (CADENAS DE CARACTERES)
 usuario = "Alfonsina"

print ("Ejemplo 6:")
if usuario == "Alfonsina":
    print("El usuario es Alfonsina")
else:
    print("El usuario no es Alfonsina")

    