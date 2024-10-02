def calcular_promedio(num_calificaciones):
    suma = 0
    for i in range(num_calificaciones):
        calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
        suma += calificacion
    promedio = suma / num_calificaciones
    return promedio

# Solicitar el número de calificaciones
num_calificaciones = int(input("Ingrese el número de calificaciones: "))

# Calcular y mostrar el promedio
promedio = calcular_promedio(num_calificaciones)
print(f"El promedio de las calificaciones es: {promedio:.2f}")
