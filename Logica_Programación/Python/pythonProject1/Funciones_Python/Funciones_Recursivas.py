# Funciones Recursivas en Python

def funcion_recursiva(numero):
    # Caso Base
    if numero == 1:
        print(numero)
    else:
        # Caso recursivo
        funcion_recursiva(numero -1)
        print(numero)


# Llamamos a la funcion 
funcion_recursiva(10)


