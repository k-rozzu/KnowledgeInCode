# Alumna: Carolina Martínez Zúñiga
# Grado y grupo: 3E
# Facultad de Ingeniería Electromecánica
# Estructura de Datos
# Simulación de supermercado
# 14 de Septiembre de 2026

from collections import deque
clientes = deque()

while True:
    print("\n== SISTEMA DE GESTIÓN DE COLAS ==")
    print("1. Agregar cliente")
    print("2. Atender cliente")
    print("3. Mostrar cola")
    print("4. Salir")

    opcion = input("\nIntroduce tu elección: ")

    if opcion == "1":
        cliente = input("\nIntroduce el nombre del cliente: ")
        pedido = input("Introduce el nombre del pedido: ")
        cliente_1 = (cliente, pedido)
        clientes.append(cliente_1)
        print(f"\nCliente agregado correctamente: {cliente_1[0]} - Pedido: {cliente_1[1]}")

    elif opcion == "2":
        if not clientes:
            print("\nLa cola está vacía. No hay clientes por atender.")
        else:
            atendido = clientes.popleft()
            print(f"\nCliente atendido: {atendido[0]} | Pedido: {atendido[1]}")
            print("Clientes restantes en cola:", len(clientes))

    elif opcion == "3":
        if not clientes:
            print("\nLa cola está vacía.")
        else:
            print("\nPedidos actuales:", list(clientes))

    elif opcion == "4":
        print("\nSaliendo del sistema...")
        break

    else:
        print("\nOpción no válida. Intenta de nuevo.")