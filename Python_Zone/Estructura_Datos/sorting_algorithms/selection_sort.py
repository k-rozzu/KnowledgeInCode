def selection_sort(lista):
    n = len(lista)

    # Recorremos la lista posición por posición
    for i in range(n):
        # Asumimos que el primer elemento no ordenado es el mínimo
        indice_minimo = i

        # Buscamos el elemento más pequeño en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j  # Actualizamos la posición del nuevo mínimo

        # Intercambiamos el mínimo encontrado con el elemento de la posición actual 'i'
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    return lista


# --- PRUEBA DEL CÓDIGO ---
numeros = [64, 25, 12, 22, 11]

print("Lista original:", numeros)
lista_ordenada = selection_sort(numeros)
print("Lista ordenada:", lista_ordenada)