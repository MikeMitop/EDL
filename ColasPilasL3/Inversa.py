from collections import deque


def invertirCola(cola: deque):
    # Caso base: si la cola está vacía, se detiene la recursión.
    if not cola:
        return

    frente = cola.popleft()

    # Llamada recursiva para invertir el resto de la cola.
    invertirCola(cola)

    # Reinserta el elemento al final de la cola.
    cola.append(frente)


def main():
    # Inicializamos la cola.
    cola = deque()

    # Agregamos los elementos 1 a 6 repetidos 5 veces.
    for num in [1, 2, 3, 4, 5, 6] * 5:
        cola.append(num)

    print("Cola original:", list(cola))

    # Invertimos la cola.
    invertirCola(cola)

    print("Cola invertida:", list(cola))


if __name__ == '__main__':
    main()
