from servicios.inventario import Inventario
from modelos.producto import Producto

def menu():
    print("\n--- Sistema de Gestión de Inventario ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Mostrar todos los productos")
    print("5. Salir")

def main():
    # Al instanciar, automáticamente llama a cargar_inventario()
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_prod = input("ID: ")
            nombre = input("Nombre: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.añadir_producto(Producto(id_prod, nombre, cantidad, precio))
            except ValueError:
                print("❌ Error: La cantidad debe ser entera y el precio numérico.")

        elif opcion == '2':
            id_prod = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == '3':
            id_prod = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            
            try:
                cant_val = int(cantidad) if cantidad.strip() else None
                prec_val = float(precio) if precio.strip() else None
                inventario.actualizar_producto(id_prod, cant_val, prec_val)
            except ValueError:
                print("❌ Error: Ingrese valores numéricos válidos.")

        elif opcion == '4':
            print("\n--- Lista de Productos ---")
            inventario.mostrar_todos()

        elif opcion == '5':
            print("Guardando y saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()