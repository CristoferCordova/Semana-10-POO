import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario() # Requisito 2: Cargar automáticamente al iniciar

    def cargar_inventario(self):
        """Lee el archivo de texto y reconstruye el inventario manejando excepciones."""
        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    # Formato esperado en el txt: id,nombre,cantidad,precio
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        try:
                            id_prod, nombre = datos[0], datos[1]
                            cantidad, precio = int(datos[2]), float(datos[3])
                            self.productos.append(Producto(id_prod, nombre, cantidad, precio))
                        except ValueError:
                            print(f"⚠️ Advertencia: Datos corruptos en la línea -> {linea.strip()}")
            print(f"✅ Inventario cargado exitosamente desde '{self.archivo}'.")
            
        except FileNotFoundError:
            # Requisito 3: Capturar FileNotFoundError y crear el archivo si no existe
            print(f"⚠️ Archivo '{self.archivo}' no encontrado. Creando un archivo nuevo...")
            try:
                open(self.archivo, 'w').close()
            except PermissionError:
                print(f"❌ Error: No se tienen permisos para crear '{self.archivo}'.")
                
        except PermissionError:
            # Requisito 3: Capturar PermissionError
            print(f"❌ Error: Permiso denegado para leer el archivo '{self.archivo}'.")
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado al leer: {e}")

    def guardar_inventario(self):
        """Guarda la lista actual de productos sobreescribiendo el archivo de texto."""
        try:
            with open(self.archivo, 'w') as file:
                for prod in self.productos:
                    linea = f"{prod.get_id()},{prod.get_nombre()},{prod.get_cantidad()},{prod.get_precio()}\n"
                    file.write(linea)
            return True
        except PermissionError:
            print(f"❌ Error de Permisos: No se puede escribir en '{self.archivo}'.")
            return False
        except Exception as e:
            print(f"❌ Error al intentar guardar el inventario: {e}")
            return False

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print("❌ Error: Ya existe un producto con ese ID.")
            return

        self.productos.append(producto)
        # Requisito 1 & 4: Reflejar en archivo y notificar éxito/fallo
        if self.guardar_inventario():
            print("✅ Producto añadido y guardado exitosamente en el archivo de inventario.")

    def eliminar_producto(self, id_producto):
        for i, prod in enumerate(self.productos):
            if prod.get_id() == id_producto:
                del self.productos[i]
                if self.guardar_inventario():
                    print("✅ Producto eliminado y cambios guardados en el archivo exitosamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for prod in self.productos:
            if prod.get_id() == id_producto:
                if nueva_cantidad is not None:
                    prod.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    prod.set_precio(nuevo_precio)
                
                if self.guardar_inventario():
                    print("✅ Producto actualizado y cambios guardados en el archivo exitosamente.")
                return
        print("❌ Error: Producto no encontrado.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return
        for prod in self.productos:
            print(prod)