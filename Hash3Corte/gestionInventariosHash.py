class Producto:
    def __init__(self, sku, nombre, descripcion, cantidad):
        self.sku = sku
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad

    def __str__(self):
        return f"SKU: {self.sku}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Cantidad: {self.cantidad}"

class TablaHashInventario:
    def __init__(self, size=10):
        self.size = size
        self.tabla = [[] for _ in range(self.size)]

    def hash_func(self, clave):
        hash_value = 0
        prime = 31
        for char in clave:
            hash_value = hash_value * prime + ord(char)
        return hash_value % self.size

    def agregar_producto(self, producto):
        indice = self.hash_func(producto.sku)
        for p in self.tabla[indice]:
            if p.sku == producto.sku:
                raise ValueError("El producto con ese SKU ya existe.")
        self.tabla[indice].append(producto)

    def buscar_producto(self, sku):
        indice = self.hash_func(sku)
        for p in self.tabla[indice]:
            if p.sku == sku:
                return p
        return None

    def actualizar_cantidad(self, sku, nueva_cantidad):
        producto = self.buscar_producto(sku)
        if producto:
            producto.cantidad = nueva_cantidad
        else:
            raise KeyError("Producto no encontrado.")

    def eliminar_producto(self, sku):
        indice = self.hash_func(sku)
        for p in self.tabla[indice]:
            if p.sku == sku:
                self.tabla[indice].remove(p)
                return
        raise KeyError("Producto no encontrado.")

    def mostrar_inventario(self):
        for i, lista in enumerate(self.tabla):
            print(f"Posición {i}:")
            for p in lista:
                print(f"  {p}")

if __name__ == "__main__":
    inventario = TablaHashInventario(10)

    while True:
        print("\n--- Menú Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar cantidad")
        print("4. Eliminar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            sku = input("SKU: ")
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            cantidad = int(input("Cantidad: "))
            try:
                inventario.agregar_producto(Producto(sku, nombre, descripcion, cantidad))
                print("Producto agregado.")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            sku = input("SKU a buscar: ")
            p = inventario.buscar_producto(sku)
            print(p if p else "Producto no encontrado.")

        elif opcion == "3":
            sku = input("SKU del producto: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            try:
                inventario.actualizar_cantidad(sku, nueva_cantidad)
                print("Cantidad actualizada.")
            except KeyError as e:
                print(e)

        elif opcion == "4":
            sku = input("SKU del producto a eliminar: ")
            try:
                inventario.eliminar_producto(sku)
                print("Producto eliminado.")
            except KeyError as e:
                print(e)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")
