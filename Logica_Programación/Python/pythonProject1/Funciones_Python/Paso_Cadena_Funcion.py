# Paso de una Cadena a una Función en Python
# Ejercicio pasar una Cadena

# En Python las cadena son inmutables
# Definir la Función
def cambio_valor(parametro):
    parametro = "Adios"


# Paso por referencia
arg_a = "Hola"
# arg_a[0] = "A"  # LAS CADENAS SON INMUTABLES
print(f"Antes llamar funcion: {arg_a}")
cambio_valor(arg_a)
print(f"Despues llamar funcion: {arg_a}")
