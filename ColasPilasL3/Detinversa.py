from collections import deque


def funcion1(P1, C1):
    """
    Función 1: Verifica si C1 es el inverso de P1.
    Compara los elementos de la pila (P1) y la cola (C1) copiadas en estructuras temporales.
    Retorna True si, al extraer los elementos, se obtiene la misma secuencia; de lo contrario, retorna False.
    """
    if len(P1) != len(C1):
        return False

    # Copiamos P1 en una pila auxiliar (lista) y C1 en una cola auxiliar (deque)
    tempStack = list(P1)
    tempQueue = deque(C1)

    while tempStack:
        if tempStack.pop() != tempQueue.popleft():
            return False
    return True


def funcion2(P1, P2):
    """
    Función 2: Crea una cola (C1) con los elementos de P1 que no están en P2.
    Recorre los elementos de P1 y verifica si cada uno se encuentra en P2.
    Si un elemento no se encuentra en P2, se agrega a la cola C1.
    """
    C1 = deque()
    for elementoP1 in P1:
        encontrado = False
        # Comparar con cada elemento de P2
        for elementoP2 in P2:
            if elementoP1 == elementoP2:
                encontrado = True
                break
        if not encontrado:
            C1.append(elementoP1)
    return C1


def mostrarPila(pila):
    """Imprime el contenido de la pila."""
    print("Pila:", pila)


def mostrarCola(cola):
    """Imprime el contenido de la cola."""
    print("Cola:", list(cola))


def main():
    # P1: Pila con elementos
    P1 = []
    P1.append(10)
    P1.append(20)
    P1.append(30)
    P1.append(40)
    P1.append(50)
    P1.append(60)

    # C1: Cola con los mismos datos que P1 pero en orden inverso
    C1 = deque()
    C1.append(60)
    C1.append(50)
    C1.append(40)
    C1.append(30)
    C1.append(20)
    C1.append(10)

    # P2: Otra pila con algunos datos adicionales
    P2 = []
    P2.append(20)
    P2.append(40)
    P2.append(60)
    P2.append(80)  # Este elemento no está en P1

    # Mostrar el contenido inicial de las estructuras
    print("Contenido inicial de las estructuras:")
    mostrarPila(P1)
    mostrarCola(C1)
    mostrarPila(P2)

    # Ejecutar función 1: Verificar si C1 es el inverso de P1
    print("\nEs C1 es el inverso de P1?", funcion1(P1, C1))

    # Ejecutar función 2: Crear una cola con los elementos de P1 que no están en P2
    resultado = funcion2(P1, P2)
    print("\nElementos de P1 que no están en P2:")
    mostrarCola(resultado)


if __name__ == '__main__':
    main()
