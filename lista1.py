# Definimos la lista inicial
lista = [20, 50, "Curso", 'Python', 3.14]

# Mostramos los valores actuales de la lista
print("Valores actuales de la lista:")
for i, valor in enumerate(lista):
    print(f"Índice {i}: {valor}")

# Pedimos dos nuevos valores al usuario
nuevo_valor1 = input("Ingresa el nuevo valor para el primer lugar: ")
nuevo_valor2 = input("Ingresa el nuevo valor para el segundo lugar: ")

# Sustituimos los valores en la lista
lista[0] = nuevo_valor1
lista[1] = nuevo_valor2

# Mostramos la lista actualizada
print("El nuevo valor de la lista es: {}".format(lista))
