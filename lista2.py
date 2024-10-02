# Creamos la lista con números del 1 al 10
lista = list(range(1, 11))

# Mostramos la lista original
print("Lista original:", lista)

# Multiplicamos los valores en las posiciones 4, 7 y 9 por 2
# Recuerda que los índices en Python comienzan en 0
lista[3] *= 2  # Posición 4
lista[6] *= 2  # Posición 7
lista[8] *= 2  # Posición 9

# Mostramos la lista actualizada
print("Lista actualizada:", lista)
