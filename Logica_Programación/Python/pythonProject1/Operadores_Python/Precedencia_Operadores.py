# Precedencia Operadores Python

# 1. Parantesis y Corchetes
# 2. Operadores unario, como -, ++, --, !
# 3. Aritmeticos *, /, + y -
# 4. Relacionales <, <=. > y >=
# 5. Igualdad == y !=
# 6. Logicos && y ||
# 7. Asignacion =, =+, -=, *=, etc

# Ejemplo. Se revisa de izquierda a derecha
a = 12 / 3 + 2 * 3 - 1
# Paso 1. Division 12 / 3 = 4
# Paso 2. Multiplicacion 2 * 3 = 6
# Paso 3. Suma 4 + 6 = 10
# Paso 4. Resta 10 - 1 = 9
print(f"Resultado {a}") # Devuelve un valor float, por que tenemos una Division.
print(" ")
print("Fin del Programa.")
