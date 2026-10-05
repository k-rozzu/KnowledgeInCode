def bubble_sort(lista):
    n = len(lista)

    # Recorremos todos los elementos de la lista
    for i in range(n):
        # El último i elemento ya está en su lugar correcto, no hace falta revisarlo
        for j in range(0, n - i - 1):

            # Comparamos elementos adyacentes: si el actual es mayor que el siguiente, se intercambian
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# --- PRUEBA DEL CÓDIGO ---
numeros = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", numeros)
lista_ordenada = bubble_sort(numeros)
print("Lista ordenada:", lista_ordenada)