# OPERACIONES CON VARIABLES DE DISTINTO TIPO

# Para realizar operaciones entre distintos tipos de datos debemos convertirlos en el dato adecuado


# Guardamos en la variable precio el input del usuario
precio_unitario = input("Ingrese el precio de lista: ")
cantidad = input("Ingresa la cantidad: ")

# Mostramos el tipo de las 2 variables creadas
print ( type(precio_unitario) )
print ( type(cantidad) )

# Convertimos los datos a un tipo numerico para poder multiplicarlos
precio_unitario = float(precio_unitario)
cantidad = float(cantidad)

# Guardamos la multiplicacion de cantidad por precio_unitario en la variable total
total = precio_unitario * cantidad

# Mostramos el total en pantala
print (total)

# Si queremos agregar un mensaje escrito antes del valor tenemos que convertir la variable total, del tipo float, a un string on str()
print ("El valor total es: " + str( total ) )





