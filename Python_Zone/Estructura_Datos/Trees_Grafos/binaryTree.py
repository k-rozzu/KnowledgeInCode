
# Representa una película dentro del árbol.
class Nodo:
    def __init__(self, titulo, calificacion):
        self.titulo = titulo
        self.calificacion = calificacion
        self.izquierdo = None
        self.derecho = None


# Organiza las películas según su calificación.
class ArbolPeliculas:
    def __init__(self):
        self.raiz = None

    # Inserta una película en la posición correspondiente.
    def insertar(self, titulo, calificacion):
        if calificacion < 1 or calificacion > 10:
            print("La calificación debe estar entre 1 y 10.")
            return

        if self.raiz is None:
            self.raiz = Nodo(titulo, calificacion)
        else:
            self._insertar_recursivo(self.raiz, titulo, calificacion)

    # Busca el lugar adecuado para insertar una película.
    def _insertar_recursivo(self, nodo, titulo, calificacion):
        if calificacion < nodo.calificacion:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(titulo, calificacion)
            else:
                self._insertar_recursivo(nodo.izquierdo, titulo, calificacion)

        elif calificacion > nodo.calificacion:
            if nodo.derecho is None:
                nodo.derecho = Nodo(titulo, calificacion)
            else:
                self._insertar_recursivo(nodo.derecho, titulo, calificacion)

        else:
            print("Ya existe una película con esa calificación.")

    # Busca una película por su calificación exacta.
    def buscar_por_calificacion(self, calificacion):
        actual = self.raiz

        while actual is not None:
            if actual.calificacion == calificacion:
                return actual.titulo

            elif calificacion < actual.calificacion:
                actual = actual.izquierdo

            else:
                actual = actual.derecho

        return None

    # Muestra las películas de menor a mayor calificación.
    def recorrido_inorden(self):
        self._inorden_recursivo(self.raiz)

    # Recorre primero la izquierda, después la raíz y finalmente la derecha.
    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo)
            print(nodo.titulo, "-", nodo.calificacion)
            self._inorden_recursivo(nodo.derecho)


# Crea el árbol y agrega algunas películas de ejemplo.
catalogo = ArbolPeliculas()

catalogo.insertar("Interestelar", 9)
catalogo.insertar("Shrek", 8)
catalogo.insertar("El padrino", 10)
catalogo.insertar("Cars", 7)
catalogo.insertar("Toy Story", 6)

# Busca una película con una calificación específica.
resultado = catalogo.buscar_por_calificacion(9)

if resultado is not None:
    print("Película encontrada:", resultado)
else:
    print("No hay películas con esa calificación.")

# Muestra todas las películas ordenadas por calificación.
print("\nCatálogo ordenado de menor a mayor:")
catalogo.recorrido_inorden()
