def insertion_sort(lista):
    # Recorremos la lista desde el segundo elemento (índice 1) hasta el final
    for i in range(1, len(lista)):
        clave = lista[i]  # El elemento actual que vamos a insertar en su lugar correcto
        j = i - 1

        # Movemos los elementos de la parte ordenada (a la izquierda) que sean
        # mayores que la clave, una posición hacia adelante
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1

        # Colocamos la clave en su posición correcta
        lista[j + 1] = clave

    return lista


# --- PRUEBA DEL CÓDIGO ---
numeros = [12, 11, 13, 5, 6]

print("Lista original:", numeros)
lista_ordenada = insertion_sort(numeros)
print("Lista ordenada:", lista_ordenada)