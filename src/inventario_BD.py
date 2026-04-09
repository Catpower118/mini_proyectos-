import json    
import os

# cargar el inventario desde el archivo JSON, si el archivo no existe o está vacío, se devuelve un diccionario vacío
def cargar_inventario():
    if not os.path.exists("inventario.json") or os.path.getsize("inventario.json") == 0:
        return {}

# si el archivo existe y no está vacío, se carga el inventario desde el archivo JSON
    with open("inventario.json", "r") as archivo:
        return json.load(archivo)

# asignamos a la variable inventario el diccionario cargado desde el archivo JSON
inventario = cargar_inventario()

# funcion para agregar productos al inventario
def agregar_producto():
    while True:
        try:
            inventario = cargar_inventario()  # recargar el inventario para asegurarnos de tener la versión más actualizada
            print("===========================")
            print("    Agregar producto")
            print("===========================")
            
            nombre_producto = input("Ingrese el nombre del producto: ").strip()
            cantidad_producto = int(input("Ingrese la cantidad del producto: ").strip())
            precio_producto = float(input("Ingrese el precio del producto: ").strip())
            
            if not nombre_producto:
                print("El nombre del producto es obligatorio. Por favor, intente de nuevo.")
                continue
            elif cantidad_producto <= 0:
                print("La cantidad debe ser un número positivo. Por favor, intente de nuevo.")
                continue
            elif precio_producto <= 0:
                print("El precio debe ser un número positivo. Por favor, intente de nuevo.")
                continue
            else:
                inventario[nombre_producto] = {
                    "cantidad": cantidad_producto,
                    "precio": precio_producto
                }
                # guarda el inventario actualizado en el JSON
                with open('inventario.json', 'w') as archivo:
                    json.dump(inventario, archivo, indent=4)
                print(f"Producto agregado: {nombre_producto}")
                
            opcion = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
            if opcion == "s":
                continue
            else:
                print("Gracias...")
                break
            
        except ValueError:
            print("Entrada inválida. Por favor, ingrese valores numéricos para la cantidad y el precio.")
            continue
        
# función para mostrar el inventario de productos        
def ver_productos():
    while True:
        try:
            inventario = cargar_inventario()
            print("===========================")
            print("  Inventario de productos")
            print("===========================")
         
            opcion = input("¿Desea mostrar el inventario de productos? (s/n): ").strip().lower()
         
            if opcion == "s":
                if not inventario:
                    print("No hay productos en el inventario.")
                else:
                    for producto, detalles in inventario.items():
                      print(f"Producto: {producto}")
                      print(f"Cantidad: {detalles['cantidad']}")
                      print(f"Precio: ${detalles['precio']:.2f}")
                      print("---------------------------")
            else:
                print("Gracias...")
                break
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        
# función para eliminar un producto del inventario        
def eliminar_producto():
    while True:
        try:
            inventario = cargar_inventario()
            print("===========================")
            print("    Eliminar producto")
            print("===========================")
            
            nombre_producto = input("Ingrese el nombre del producto a eliminar: ").strip()
            
            if not nombre_producto in inventario:
                print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")
                continue
            elif nombre_producto in inventario:
                del inventario[nombre_producto]
                with open('inventario.json', 'w') as archivo:
                    json.dump(inventario, archivo, indent=4)
                print(f"producto '{nombre_producto}' eliminado del inventario.")
                
            opcion = input("¿Desea eliminar otro producto? (s/n): ").strip().lower()
            if opcion == "s":
                continue
            else:
                print("Gracias...")
                break
            
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        
# función para buscar un producto en el inventario        
def buscar_producto():
    while True:
        try:
            inventario = cargar_inventario()
            print("===========================")
            print("    Buscar producto")
            print("===========================")
            
            nombre_producto = input("Ingrese el nombre del producto a buscar: ").strip()
            
            if not nombre_producto in inventario:
                print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")
                continue
            else:
                detalles = inventario[nombre_producto]
                print(f"Producto: {nombre_producto}")
                print(f"Cantidad: {detalles['cantidad']}")
                print(f"Precio: ${detalles['precio']:.2f}")
                
            opcion = input("¿Desea buscar otro producto? (s/n): ").strip().lower()
            if opcion == "s":
                continue
            else:
                print("Gracias...")
                break
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        
# función para mostrar el menú de opciones del inventario        
def inventario_menu():
    while True:
        try:
            inventario = cargar_inventario()
            print("===========================")
            print("  Menú de Inventario")
            print("===========================")
            print("1. Agregar producto")
            print("2. Ver productos")
            print("3. Eliminar producto")
            print("4. Buscar producto")
            print("5. Salir")
        
            opcion = input("Seleccione una opción (1-5): ").strip()
        
            if opcion == "1":
                agregar_producto()
            elif opcion == "2":
                ver_productos()
            elif opcion == "3":
                eliminar_producto()
            elif opcion == "4":
                buscar_producto()
            elif opcion == "5":
                print("Saliendo del menú de inventario...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida (1-5).")
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        finally:
            print("Operación finalizada.")
            
# ejecutar la funcion principal del programa para mostrar el menú de inventario            
inventario_menu()
            