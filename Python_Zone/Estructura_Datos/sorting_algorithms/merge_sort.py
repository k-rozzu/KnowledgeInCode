# --- IMPLEMENTACIÓN DE LA BÚSQUEDA BINARIA ---
def busqueda_binaria(lista_ordenada, elemento_buscado):
    inicio = 0
    fin = len(lista_ordenada) - 1
    flag = 0

    while inicio <= fin:
        medio = inicio + (fin - inicio) // 2  # Usamos // para división entera en Python

        if lista_ordenada[medio] == elemento_buscado:
            return medio  # Elemento encontrado, retorna el índice
        elif lista_ordenada[medio] < elemento_buscado:
            inicio = medio + 1  # Descarta la mitad izquierda
        else:
            fin = medio - 1  # Descarta la mitad derecha

    flag += 1
    print("Numero de ciclos: ", flag)
    return -1  # Elemento no encontrado

def merge_sort(A):
    if len(A) <= 1:
        return A
    medio = len(A) // 2
    izquierda = A[:medio]
    derecha = A[medio:]
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    return mezclar(izquierda, derecha)


def mezclar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


# --- PRUEBA DEL CÓDIGO ---
A = [7, 9, 2, 4, 6, 8, 3]
print("Lista original:", A)

# 1. Primero ordenamos la lista
lista_ordenada = merge_sort(A)
print("Lista ordenada:", lista_ordenada)

# 2. Realizamos búsquedas binarias sobre la lista ordenada
elemento = 6
print("El elemento que buscamos es:", elemento)
posicion = busqueda_binaria(lista_ordenada, elemento)

if posicion != -1:
    print(f"El elemento {elemento} se encuentra en el índice {posicion} de la lista ordenada.")
else:
    print(f"El elemento {elemento} no existe en la lista.")
