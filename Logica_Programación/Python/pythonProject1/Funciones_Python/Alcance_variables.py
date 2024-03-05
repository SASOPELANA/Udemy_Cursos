# Alcance de Variables en Python

variables_global = 5
a = 10

# Acceder a las variables 
variables_global = 10
print(variables_global)


# Definimos una funcion

def mi_funcion(variables_local):
    print(variables_local)
    # Culaquier cambio posterior no afecta el valor de la variables externa
    variables_local = 20
    # Accedemos a la variable global
    global a
    a = 30


mi_funcion(variables_global)

print(f"Variables global: {variables_global}")
print(f"Variable global: {a}")
