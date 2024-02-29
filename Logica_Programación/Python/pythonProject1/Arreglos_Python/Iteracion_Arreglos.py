# Iteración de Arreglos en Python

numeros_arreglos = [13, 14, "Hola"]
# Iterar los elementos

print("Impresion del arreglo.")

for elemento in numeros_arreglos:
    print(f"Arreglo {elemento}")

print(" ")

# Iteramos de otra forma la lsita.
print("Imprimimos de otra forma la lista.")
for indice, elemento in enumerate(numeros_arreglos):
    print(f"Arreglo[{indice}] = {elemento}")

    

