# Alumno: Carolina Martínez Zúñiga
# Grado, Grupo y Carrera: Ingeniería de Software. 3E
# Materia: Estructura de datos
# Maestro: Ernesto Navarro
# Actividad: El conjunto potencia
# Martes 01 de Septiembre de 2026


# Función para subconjuntos (con parámetros de lista)
def subconjuntos(lista):

    # contador de subconjuntos
    subc = [[]]
    # contador de iteraciones del ciclo
    i_ciclo = 0

    # recorrer los elementos de la lista
    for elemento in lista:

        # Guardamos el número actual de subconjuntos
        n_actual = len(subc)

        # Iteramos únicamente sobre los subconjuntos que ya teníamos construidos
        for i in range(n_actual):
            i_ciclo += 1

            # Tomamos un subconjunto existente y le añadimos el nuevo elemento
            nuevo_subconjunto = subc[i] + [elemento]

            # Agregamos el nuevo subconjunto a nuestra lista global de resultados
            subc.append(nuevo_subconjunto)

    return subc, i_ciclo

# nuestra lista de enteros
lista = [9, 0, 8, 4]

# guardar el total de subconjuntos y de iteraciones del ciclo
resultado, total_iteraciones = subconjuntos(lista)

# imprimir resultados
print(f"Lista original ({len(lista)} elementos): {lista}")
print(f"Subconjuntos ({len(resultado)} en total): {resultado}")
print(f"Total de iteraciones del ciclo interno: {total_iteraciones}")


''' El numero de iteraciones que recorra el ciclo, corresponderá a nuestra unidad 2
elevada al número de elementos de la lista, restando 1. Es decir: (2^n) - 1.
Ej: si tenemos una lista de 3 elementos, el número de iteraciones será: (2^3)-1 = 7.
Esto corresponde a O(2^n).

Si n = 10, será: (2^10)-1 = 1024 - 1 = 1023.
Si n = 20, será: (2^20)-1 = 1048576 - 1 = 1048575
Si n = 30, será: (2^30)-1 = 1073741824 - 1 = 1073741823.

Y así sucesivamente....
'''