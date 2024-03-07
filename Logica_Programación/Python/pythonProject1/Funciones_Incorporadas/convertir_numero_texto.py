# Convertir un Número a Texto en Python

a, b = 10, 20

# Si son numeros se suman
print(a + b)


# Convertir a cadena
concatenacion = str(a) + str(b)
print(concatenacion)

concatenacion = a.__str__() + b.__str__()
print(concatenacion)

# metodo repr
concatenacion = a.__repr__() + b.__repr__()
print(concatenacion)
