import random

class Producto:
    def __init__(self, codigo, cantidad, precio, count=1):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio = precio
        self.count = count

    def __str__(self):
        return f"Código: {self.codigo:4d} | Cantidad: {self.cantidad:3d} | Precio: {self.precio:6.2f}"

def poblar_datos(lista, n):
    for _ in range(n):
        producto = Producto(
            random.randint(1000, 9999),
            random.randint(1, 10),
            round(random.uniform(10, 200), 2)
        )
        lista.append(producto)

def mostrar_datos(lista):
    for producto in lista:
        print(producto)

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].codigo > lista[j + 1].codigo:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def suma_ventas(lista_entrada, lista_salida):
    bubble_sort(lista_entrada)  

    if not lista_entrada:
        return

    ultimo_producto = lista_entrada[0]

    for producto_actual in lista_entrada[1:]:
        if producto_actual.codigo == ultimo_producto.codigo:
            nuevo_count = ultimo_producto.count + 1
            nuevo_precio = round(
                (ultimo_producto.precio * ultimo_producto.count + producto_actual.precio)
                / nuevo_count, 2
            )
            ultimo_producto = Producto(
                ultimo_producto.codigo,
                ultimo_producto.cantidad + producto_actual.cantidad,
                nuevo_precio,
                nuevo_count
            )
        else:
            lista_salida.append(ultimo_producto)
            ultimo_producto = producto_actual

    lista_salida.append(ultimo_producto)
    lista_entrada.clear()

if __name__ == "__main__":
    print("Lista Productos Vendidos Totalizada")
    print("=" * 50)

    ventas = []
    totalizadas = []

    poblar_datos(ventas, 15)

    print("\nDatos  originales:")
    print("-" * 50)
    mostrar_datos(ventas)

    suma_ventas(ventas, totalizadas)

    print("\nDatos de ventas totales por producto:")
    print("-" * 50)
    mostrar_datos(totalizadas)
