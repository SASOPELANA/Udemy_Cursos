# Operador Ternario Python

mi_numero = int(input("Proporciones un numero: "))
# Revisar si el numero es mayor que cero.
if mi_numero > 0:
    print(f"Valor positivo: {mi_numero}")
else:
    print(f"Valor cero o negativo: {mi_numero}")

# Operador Ternario
print()
print("Positivo") if mi_numero > 0 else print("Cero o Negativo")
