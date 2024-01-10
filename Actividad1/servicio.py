from .producto import Producto
class Servicio:

    #Productos de ejemplo
    p1 = Producto("Manzana",0.2,200,True,"0001")
    p2 = Producto("Pera",0.15,200,True,"0002")
    p3 = Producto("Piña",3.5,100,True,"0003")
    p4 = Producto("Sandía",4.25,50,True,"0004")

    diccionario_productos = {
        p1.codigo:p1,
        p2.codigo:p2,
        p3.codigo:p3,
        p4.codigo:p4
    }

    #En esta lista se van almacenando los productos que deseas comprar.
    lista_compra = []

    #Agregar productos al inventario.
    def agregar_producto_inventario(self,producto):
        self.diccionario_productos[producto.codigo] = producto

    #Mostrar diccionario de productos.
    def mostrar_inventario(self):
        for codigo, producto in self.diccionario_productos.items():
            print(f"Código: {codigo}, Producto: {producto.nombre}, Stock: {producto.stock}")

    #Añade producto a la lista de la compra.
    def agregar_producto_compra(self,producto):
        self.lista_compra.append(producto)

    #Realizar compra de productos.
    def realizar_compra(self):
        total = 0
        for elemento in self.lista_compra.count():
            total += elemento.precio
        return total