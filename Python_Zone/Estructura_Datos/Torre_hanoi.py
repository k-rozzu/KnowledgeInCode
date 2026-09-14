# Inicializar las 3 torres (listas)
torre1 = [3, 2, 1]  # El 1 está en la cima
torre2 = []
torre3 = []

# Guardar todas las torres juntas para acceder a ellas fácilmente
torres = [torre1, torre2, torre3]

# Contador de movimientos válidos
movimientos = 0

# Bucle principal: se repite hasta que la torre 3 tenga los 3 discos
while len(torre3) < 3:
    # Mostrar el estado actual de las torres y el contador
    print("\n--- ESTADO DE LAS TORRES ---")
    print("Torre 1:", torre1)
    print("Torre 2:", torre2)
    print("Torre 3:", torre3)
    print("Movimientos realizados:", movimientos)

    # Pedir al usuario la torre de origen
    origen = int(input("\n¿De qué torre quieres MOVER el disco? (1, 2 o 3): ")) - 1

    # Validar que la torre elegida tenga discos (no esté vacía)
    if len(torres[origen]) == 0:
        print("¡Error! La torre elegida está vacía.")
        continue

    # Pedir al usuario la torre de destino
    destino = int(input("¿A qué torre quieres PONER el disco? (1, 2 o 3): ")) - 1

    # Obtener el disco que se quiere mover (el de la cima)
    disco_a_mover = torres[origen][-1]

    # Comprobar si la torre destino tiene discos y ver su disco superior
    if len(torres[destino]) > 0:
        disco_destino = torres[destino][-1]
        # Regla: NO se puede poner un disco grande sobre uno chico
        if disco_a_mover > disco_destino:
            print("¡Movimiento inválido! No puedes poner un disco grande sobre uno chico.")
            continue

    # Hacer el movimiento: desapilar del origen y apilar en el destino
    disco = torres[origen].pop()
    torres[destino].append(disco)

    # Sumar un movimiento solo cuando la jugada fue válida
    movimientos += 1

# Mensaje final al ganar con el total de movimientos
print("\n¡Felicidades! Has completado la Torre de Hanoi en la Torre 3.")
print("Total de movimientos:", movimientos)
print("\nTorre 1:", torre1)
print("Torre 2:", torre2)
print("Torre 3:", torre3)


'''
== PARTIDA 1 (TORRE DE 3 ELEMENTOS)(MOVIMIENTOS EXPECTADOS: 7) ==

--- ESTADO DE LAS TORRES ---
Torre 1: [3, 2, 1]
Torre 2: []
Torre 3: []
Movimientos realizados: 0

¿De qué torre quieres MOVER el disco? (1, 2 o 3): 1
¿A qué torre quieres PONER el disco? (1, 2 o 3): 3

--- ESTADO DE LAS TORRES ---
Torre 1: [3, 2]
Torre 2: []
Torre 3: [1]
Movimientos realizados: 1

¿De qué torre quieres MOVER el disco? (1, 2 o 3): 1
¿A qué torre quieres PONER el disco? (1, 2 o 3): 2

--- ESTADO DE LAS TORRES ---
Torre 1: [3]
Torre 2: [2]
Torre 3: [1]
Movimientos realizados: 2

¿De qué torre quieres MOVER el disco? (1, 2 o 3): 3
¿A qué torre quieres PONER el disco? (1, 2 o 3): 2

--- ESTADO DE LAS TORRES ---
Torre 1: [3]
Torre 2: [2, 1]
Torre 3: []
Movimientos realizados: 3

¿De qué torre quieres MOVER el disco? (1, 2 o 3): 1
¿A qué torre quieres PONER el disco? (1, 2 o 3): 3

--- ESTADO DE LAS TORRES ---
Torre 1: []
Torre 2: [2, 1]
Torre 3: [3]
Movimientos realizados: 4

¿De qué torre quieres MOVER el disco? (1, 2 o 3): 2
¿A qué torre quieres PONER el disco? (1, 2 o 3): 1

--- ESTADO DE LAS TORRES ---
Torre 1: [1]
Torre 2: [2]
Torre 3: [3]
Movimientos realizados: 5

¿De qué torre quieres MOVER el disco? (1, 2 o 3): 2
¿A qué torre quieres PONER el disco? (1, 2 o 3): 3

--- ESTADO DE LAS TORRES ---
Torre 1: [1]
Torre 2: []
Torre 3: [3, 2]
Movimientos realizados: 6

¿De qué torre quieres MOVER el disco? (1, 2 o 3): 1
¿A qué torre quieres PONER el disco? (1, 2 o 3): 3

¡Felicidades! Has completado la Torre de Hanoi en la Torre 3.
Total de movimientos: 7

Torre 1: []
Torre 2: []
Torre 3: [3, 2, 1]

Process finished with exit code 0

'''