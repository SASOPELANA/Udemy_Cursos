import math

# Redondeo y Truncado en Python

numero = 8.5
print(f"Valor original: {numero}")

# round() - Redondeo al entero por mas cercano

redondeo = round(numero)
print(f"Redondeo: {redondeo}")

# Truncado, elimina los decimales
truncado = math.trunc(numero)
print(f"Truncado: {truncado}")

# math.floor()   redondea al entero inferior mas cercano
floor = math.floor(numero)
print(f"Floor. {floor}")

# math.ceil()  redondea al entero superior mas cercano
ceil = math.ceil(numero)
print(f"Ceil: {ceil}")

