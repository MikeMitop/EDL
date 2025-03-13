from collections import deque


def eliminarElemento(cola: deque, dato: int):
    # Caso base: si la cola está vacía, termina la recursión.
    if not cola:
        return

    # Extrae el primer elemento de la cola.
    frente = cola.popleft()

    # Llamada recursiva para procesar el resto de la cola.
    eliminarElemento(cola, dato)

    # Si el elemento extraído no es el que se quiere eliminar, se vuelve a insertar.
    if frente != dato:
        cola.append(frente)


def ordenar(cola: deque):
    # Caso base: si la cola está vacía, termina la recursión.
    if not cola:
        return

    # Extrae el primer elemento de la cola.
    frente = cola.popleft()

    # Llamada recursiva para procesar el resto de la cola.
    ordenar(cola)

    # Reinsertamos el elemento para restaurar el orden original.
    cola.append(frente)


def main():
    # Inicializamos la cola y la llenamos con los valores indicados.
    cola = deque()

    # Agregamos secuencialmente los elementos; en el ejemplo Java se agregaron los números 1,2,3,4,5,6 repetidos varias veces.
    # Aquí simulamos el mismo comportamiento agregando la secuencia 1-6 cinco veces.
    for num in [1, 2, 3, 4, 5, 6] * 5:
        cola.append(num)

    datoAEliminar = 3
    print("Cola original:", list(cola))

    # Se elimina el dato y luego se reordena la cola para mantener el orden original.
    eliminarElemento(cola, datoAEliminar)
    ordenar(cola)

    print("Cola después de eliminar", datoAEliminar, ":", list(cola))


if __name__ == '__main__':
    main()
