# Sentencias if - else en Python

mi_numero = int(input("Proporciones un numero: "))
# Revisar si el numero es mayor que cero.
if mi_numero > 0:
    print(f"Valor positivo: {mi_numero}")
elif mi_numero < 0:
    print(f"Valor negativo: {mi_numero}")
else:
    print(f"Valor cero: {mi_numero}")
