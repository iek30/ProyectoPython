from producto import Producto

class Servicio:
    def __init__(self):
        # Productos de ejemplo
        self.p1 = Producto("Manzana", 0.2, 200, True, "0001")
        self.p2 = Producto("Pera", 0.15, 200, True, "0002")
        self.p3 = Producto("Piña", 3.5, 100, True, "0003")
        self.p4 = Producto("Sandía", 4.25, 50, True, "0004")

        # Diccionario de productos
        self.diccionario_productos = {
            self.p1.codigo: self.p1,
            self.p2.codigo: self.p2,
            self.p3.codigo: self.p3,
            self.p4.codigo: self.p4
        }

        # Lista de compra
        self.lista_compra = []

    def agregar_producto_inventario(self, producto):
        self.diccionario_productos[producto.codigo] = producto

    def mostrar_inventario(self):
        for codigo, producto in self.diccionario_productos.items():
            print(f"Código: {codigo}, Producto: {producto.nombre}, Stock: {producto.stock}")

    def agregar_producto_compra(self, producto):
        if producto.cantidad > 0:
            self.lista_compra.append(producto)
            producto.cantidad = producto.cantidad-1
            if producto.cantidad == 0: producto.stock = False

    def realizar_compra(self):
        total = 0
        for elemento in self.lista_compra:
            total += elemento.precio
        return total
