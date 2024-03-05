# Paso por valor en Python
# Ejercicio paso por valor

# Definir la funcion
def cambio_valor(parametro):
    parametro = 50

# Paso por valor
arg_a = 10
print(f"Antes llamar funcion: {arg_a}")
cambio_valor(arg_a)
print(f"Despues llamar funcion: {arg_a}")

