# Sumar 5 números con el ciclo while en Python

numero, minimo, maximo = 1, 0, 5
acumuladorSuma = 0

while numero <= maximo:
    print(f"{acumuladorSuma} + {numero}")
    acumuladorSuma += numero
    print(f"Suma Parcial es: {acumuladorSuma}")
    numero += 1

print(f"La suma de los primeros {maximo} numeros es: {acumuladorSuma}")    
