def quicksort(lista):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista

    # Elegimos el pivote (en este caso, el elemento central)
    pivote = lista[len(lista) // 2]

    # Dividimos la lista en tres partes según el pivote
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]

    # Ordenamos recursivamente los menores y mayores, y los unimos
    return quicksort(menores) + iguales + quicksort(mayores)


# --- PRUEBA DEL CÓDIGO ---
numeros = [29, 10, 14, 37, 14, 20, 7, 2]

print("Lista original:", numeros)
lista_ordenada = quicksort(numeros)
print("Lista ordenada:", lista_ordenada)