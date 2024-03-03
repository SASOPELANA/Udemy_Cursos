# Función para Sumar en Python

# 1. Declarar la funcion Sumar

def sumar(a, b):
    resultado_suma = a + b
    return resultado_suma

# 2. Llamar la funcion sumar

arg_a = int(input("Valor a: "))
arg_b = int(input("Valor b: "))

# Llamamos la funcion
resultado = sumar(arg_a, arg_b)
print(f"Resultado suma: {resultado}")
