# Introducir valores en Python

#nombre = input("Proporciona tu nombre: ")
#print(f"Tu nombre es: {nombre}")

# Proporciona un valor entero
numero_str = input("Proporciona un numero entero: ")
print(f"El numero {numero_str} es de tipo: {type(numero_str)}")

# Lo convertimos a entero
numero = int(numero_str)
print(f"El numero {numero} es de tipo: {type(numero)}")
 
# Obtenemos directamente un valor entero
entero = int(input("Proporciona un numero: "))
print(f"El numero {entero} es de tipo: {type(entero)}")
