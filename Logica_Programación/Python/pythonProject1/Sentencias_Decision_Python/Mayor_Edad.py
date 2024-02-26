# Algoritmo Mayor de Edad en Python.

EDAD_ADULTO = 18
edad = int(input("Proporciona tu edad: "))

# Revisamos si es mayor de edad
if edad >= EDAD_ADULTO:
    print(f"Eres mayor de edad: {edad}")
else:
    print(f"Eres menor de edad: {edad}")

print()
print("Algoritmo para verificar contraseñas.")
CONTRASEÑA = 89352
num = int(input("Proporciona tu contraseña: "))
if num == CONTRASEÑA:
    print(f"Acesso Permitido. Bienvenido.")
else:
    print(f"Acesso Denegado. Usted no esta registrado.")
print()
print("--FIN DEL PROGRAMA--")
