# Capturar o Ingrsar Valores en un Arreglo. Python
arreglo = []


# Solicitamos el tamaño del arreglo
no_elementos = int(input("No. Elementos de Arreglo: "))
# Iteramos para solicitar los valores del arreglo.
for indice in range(no_elementos):
    valor = int(input(f"Arreglo[{indice}] = "))
    # arreglo[indice] = valor # nos arroja un error
    arreglo.append(valor)


# Iteramos de otra forma la lista
print("Imprimimos de otra forma la lista")
for indice in range(len(arreglo)):
    print(f"Arreglo[{indice}] = {arreglo[indice]}")
    
