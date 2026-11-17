class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


if __name__ == "__main__":
    ht = HashTable(capacity=3)

    ht.insert("nombre", "Ana")
    ht.insert("edad", 25)
    ht.insert("ciudad", "Madrid")
    ht.insert("pais", "España")
    ht.insert("nombre", "Carlos")

    print("Estado interno de la tabla:")
    for i, bucket in enumerate(ht.table):
        print(f"Índice {i}: {bucket}")

    print("\nPruebas de búsqueda:")
    print("nombre ->", ht.get("nombre"))
    print("ciudad ->", ht.get("ciudad"))
    print("telefono ->", ht.get("telefono"))

    print("\nEliminando 'edad':", ht.remove("edad"))
    print("edad ->", ht.get("edad"))

    print("\nEstado final de la tabla:")
    for i, bucket in enumerate(ht.table):
        print(f"Índice {i}: {bucket}")