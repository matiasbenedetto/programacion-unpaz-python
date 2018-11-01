# BLOQUES DE CODIGO ANIDADOS

# En Python podemos anidar bloques de codigo utilizando la indentación o sangrado.

# Ejemplo1: Vamos a implementar un programa que efectue distintos descuentos sobre un precio:
#  Condiciones: 
#    * Los clientes frecuentes se les aplica un descuento de 50
#    * Los clientes frecuentes tienen un descuento de 100 cuando el precio es mayor a 400
#    * El resto de los clientes tienen un descuento de 15


#Creamos las variables
precio = 500
cliente_frecuente = False

# Verificamos si el cliente es frecuente o no
if cliente_frecuente:
    print("Es cliente frecuente")
    # Si el cliente es frecuente verificamos si el precio es mayor a 400 o no
    if precio > 400:
        descuento = 100
    else:
        descuento = 50
# Si no es cliente frecuente
else:
    print("No es cliente frecuente")
    descuento = 15

total = precio - descuento
print(total)

