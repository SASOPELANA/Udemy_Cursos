# Iterar una Matriz en Python
# Usamos la sintaxis simplificada

matriz = [[100, 200, 300],[400, 500, 600]]

# Iterar la Matriz 
renglones = len(matriz)
columnas = len(matriz[0])

for ren in range(len(matriz)):
    for col in range(len(matriz[ren])):
        print(f"Matriz [{ren}][{col}] = {matriz[ren][col]}")
