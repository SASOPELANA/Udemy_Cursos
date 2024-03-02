# Introducir Valores a una Matriz en Python

renglones = int(input("Proporciona no. Renglones(Filas): "))
columnas = int(input("Proporciona no.   Columnas: "))

# Creamos la Matriz

matriz = [0] * renglones

for ren in range(renglones):
    # Por cada renglon, asignamos una lista de m columnas.
    matriz[ren] = [0] * columnas
# print(f"Matriz creada: {matriz}")    
    
# Solicitamos los valores de manera dinamica
for ren in range(renglones):
    for col in range(columnas):
        matriz[ren][col] = int(input(f"Matriz [{ren}][{col}] = "))

print(" ")

print("Inpresion de Matriz: ")

# Imprimimos la matriz
for ren in range(renglones):
    for col in range(columnas):
        print(f"Matriz [{ren}][{col}] = {matriz[ren][col]}")
    print()    

