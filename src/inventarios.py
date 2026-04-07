
# diccionario para almacenar el inventario de productos funcionara como una BD temporal
inventario = {}

# función para agregar un producto al inventario
def agregar_producto():
    while True:
        try:
            print("===========================")
            print("    Agregar producto")
            print("===========================")
            
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad_producto = int(input("Ingrese la cantidad del producto: "))
            precio_producto = float(input("Ingrese el precio del producto: "))
            
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
                print(f"Producto '{nombre_producto}' agregado al inventario.")
                
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
def mostar_inventario():
    while True:
        try:
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
            print("===========================")
            print("    Eliminar producto")
            print("===========================")
            
            nombre_producto = input("Ingrese el nombre del producto a eliminar: ").strip()
            if nombre_producto in inventario:
                del inventario[nombre_producto]
                print(f"producto '{nombre_producto}' eliminado del inventario.")
            else:
                print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")
            
            opcion = input("Desea eliminar otro producto? (s/n): ").strip().lower()
            if opcion == "s":
                continue
            else:
                print("Gracias...")
                break
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        
def buscar_producto():
    while True:
        try:
            print("===========================")
            print("    Buscar producto")
            print("===========================")
            
            nombre_producto = input("Ingrese el nombre del producto a buscar: ").strip()
            
            if not nombre_producto in inventario:
                print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")
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
        finally:
            print("Operación de búsqueda finalizada.")        
        
# funcion padre para mostrar el menu de inventario y llamar a las funciones correspondientes        
def inventario_menu():
    while True:
        try:
            print("========================")
            print("  Menú de inventario")
            print("========================")
            print("1. Agregar producto")
            print("2. Mostrar inventario")
            print("3. Eliminar producto")
            print("4. Buscar producto")
            print("5. Salir")
            
            opcion = input("Seleccione una opción (1-4): ").strip().lower()
            
            if opcion == "1":
                agregar_producto()
            elif opcion == "2":
                mostar_inventario()
            elif opcion == "3":
                eliminar_producto()
            elif opcion == "4":
                buscar_producto()
            elif opcion == "5":
                print("Gracias...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida (1-5).")
                continue
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        
inventario_menu()
            