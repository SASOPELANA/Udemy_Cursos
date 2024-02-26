# Algoritmo Dia de la Semana en Python.

dia_semana = int(input("Proporcione el dia de la semana (1-7): "))
# Revisamos el dia de la semana.

if dia_semana == 1:
    print("Lunes.")
elif dia_semana == 2:
    print("Martes.")
elif dia_semana == 3:
    print("Miercoles.")
elif dia_semana == 4:
    print("Jueves.")
elif dia_semana == 5:
    print("Viernes.")
elif dia_semana == 6:
    print("Sabado.")
elif dia_semana == 7:
    print("Domingo.")
else:
    print(f"Error. Dia no valido. {dia_semana}")    
