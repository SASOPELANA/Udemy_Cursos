# Sumar los primeros 5 números Ciclo for en Python.

acuamulador_suma = 0
for numero in range(1, 6):
    print(f"{acuamulador_suma} + {numero}")
    acuamulador_suma += numero
    print(f"Suma parcial {acuamulador_suma}")

print(f"La suma de los primeros 5 numeros es: {acuamulador_suma}")
