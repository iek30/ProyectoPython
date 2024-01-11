from servicio import Servicio
from producto import Producto
import sys

servicio = Servicio()

while True:
    print("__MENÚ__")
    print("1.Agregar a inventario.")
    print("2.Agregar al carrito.")
    print("3.Realizar compra.")
    print("4.Mostrar inventario.")
    print("5.Salir")
    respuesta = input("Debes de seleccionar una opción: ")
    if respuesta == "1":
        #Producto de ejemplo
        p = Producto("Lechuga",0.5,230,True,"0005")
        servicio.agregar_producto_inventario(p)
    elif respuesta == "2":
        p = Producto("Lechuga",0.5,230,True,"0005")
        servicio.agregar_producto_compra(p)
    elif respuesta == "3":
        print(servicio.realizar_compra())
    elif respuesta == "4":
        servicio.mostrar_inventario()
    else:
        sys.exit()