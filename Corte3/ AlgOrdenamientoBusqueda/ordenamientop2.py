import random

def llenarDatos(ids, nombres, datos, n):
    lista_nombres = ["Juanita", "Pachita", "Albita", "Pedrito", "Damaris", 
                     "Juan", "Miguel", "Julian", "Andres", "Diego"]
    for k in range(n):
        id_emp = random.randint(1000, 9999)
        nombre = lista_nombres[random.randint(0, len(lista_nombres) - 1)]
        sueldo = random.randint(1000, 5000)
        max_deducciones = int(sueldo * 0.3)
        deducciones = random.randint(0, max_deducciones)
        neto = sueldo - deducciones
        ids.append(id_emp)
        nombres.append(nombre)
        datos.append([sueldo, deducciones, neto])

def ordenarPorIdentificacion(ids, nombres, datos):
    for i in range(len(ids) - 1):
        pos_min = i
        for j in range(i + 1, len(ids)):
            if ids[j] < ids[pos_min]:
                pos_min = j
        if pos_min != i:
            ids[i], ids[pos_min]         = ids[pos_min], ids[i]
            nombres[i], nombres[pos_min] = nombres[pos_min], nombres[i]
            datos[i], datos[pos_min]     = datos[pos_min], datos[i]

def quicksort(ids, nombres, datos, izq, der):
    if izq < der:
        piv = nombres[(izq + der) // 2]
        i = izq
        j = der
        while i <= j:
            while nombres[i] < piv:
                i += 1
            while nombres[j] > piv:
                j -= 1
            if i <= j:
                nombres[i], nombres[j] = nombres[j], nombres[i]
                ids[i], ids[j]         = ids[j], ids[i]
                datos[i], datos[j]     = datos[j], datos[i]
                i += 1
                j -= 1
        quicksort(ids, nombres, datos, izq, j)
        quicksort(ids, nombres, datos, i, der)

def mostrarDatos(ids, nombres, datos):
    print(f"{'ID':<8} {'Nombre':<10} {'Sueldo':>10} {'Deducciones':>12} {'Neto':>10}")
    print("-" * 50)
    for i in range(len(ids)):
        print(f"{ids[i]:<8} {nombres[i]:<10} {datos[i][0]:>10d} {datos[i][1]:>12d} {datos[i][2]:>10d}")
    print("-" * 50)

def main():
    ids = []
    nombres = []
    datos = []
    n = 10
    llenarDatos(ids, nombres, datos, n)

    print("\nNómina sin ordenar:")
    mostrarDatos(ids, nombres, datos)

    ordenarPorIdentificacion(ids, nombres, datos)
    print("\nNómina ordenada por identificación:")
    mostrarDatos(ids, nombres, datos)

    quicksort(ids, nombres, datos, 0, len(ids) - 1)
    print("\nNómina ordenada por nombre:")
    mostrarDatos(ids, nombres, datos)

if __name__ == "__main__":
    main()
