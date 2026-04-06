import json
import os        

# funcion para cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    # Si no existe o está vacío, devolvemos una lista vacía
    if not os.path.exists("usuarios.json") or os.path.getsize("usuarios.json") == 0:
        return []

    with open("usuarios.json", "r") as archivo:
        return json.load(archivo)
    
# asignamos a la variable usuarios la lista de usuarios cargada desde el archivo JSON
usuarios = cargar_usuarios()

# función para registrar los datos de un nuevo estudiante    
def registrar_datos():
    while True:
        try:
            print("---------------------------------")
            print("    Registro de estudiantes")
            print("---------------------------------")
            nombre = input("Ingrese el nombre del estudiante: ").strip()
            apellido = input("Ingrese el apellido del estudiante: ").strip()
            edad = input("Ingrese la edad del estudiante: ").strip()
            ciudad = input("Ingrese la ciudad del estudiante: ").strip()

            if not nombre or not apellido or not edad or not ciudad:
                print("Todos los campos son obligatorios. Por favor, intente de nuevo.")
                continue
            if not edad.isdigit():
                print("La edad debe ser un número. Por favor, intente de nuevo.")
                continue
            if int(edad) <= 0:
                print("La edad debe ser un número positivo. Por favor, intente de nuevo.")
                continue

            # Agregar estudiante a la lista
            usuarios.append({
                "nombre": nombre,
                "apellido": apellido,
                "edad": int(edad),
                "ciudad": ciudad
            })

            # Guardar en JSON
            with open('usuarios.json', 'w') as archivo:
                json.dump(usuarios, archivo, indent=4)
                print("Datos registrados exitosamente.")
            
            opcion = input("¿Desea registrar otro estudiante? (s/n): ").strip().lower()
            if opcion != 's':
                break
            else:
                continue

        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        
# función para mostrar la lista de estudiantes registrados        
def mostar_usuarios():
    while True:
        try:
            print("===============================")
            print("    lista de estudiantes")
            print("================================")
            
            opcion = input("¿Desea mostrar la lista de estudiantes? (s/n): ").strip().lower()
            
            if opcion == "s":
                if not usuarios:
                    print("No hay estudiantes registrados.")
                else:
                    for idx, usuario in enumerate(usuarios, start=1):
                        print(f"{idx}. {usuario['nombre']} {usuario['apellido']}, Edad: {usuario['edad']}, Ciudad: {usuario['ciudad']}")
            else:
                print("Gracias...")
                break
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        
# función para eliminar un estudiante registrado        
def eliminar_usuario():
    while True:
        try:
            print("===============================")
            print("    Eliminar estudiante")
            print("================================")
            
            opcion = input("Nombre del estudiante a elimnar: ").strip()
            opcion_apellido = input("Apellido del estudiante a eliminar: ").strip()
            
            encontrar = [
              u for u in usuarios 
                if u["nombre"].lower() == opcion.lower() and u["apellido"].lower() == opcion_apellido.lower()
            ]

            if not encontrar:
                print("Usuario no encontrado. por favor, intente de nuevo.") 
            else:
                usuarios.remove(encontrar[0])
                with open('usuarios.json', 'w') as archivo:
                    json.dump(usuarios, archivo, indent=4)
                print("Usuario eliminado exitosamente.")
            
            opcion_2 = input("Desea eliminar otro usuario? (s/n): ").strip().lower()
            
            if opcion_2 == "s":
                continue
            else:
                break
        except Exception as e:
            print(f"Ocurrió un error: {e}. Por favor, intente de nuevo.")
            continue
        finally:
            print("Gracias por usar el sistema de registro...")    
                       
# función principal del programa que muestra el menú de opciones para el registro de estudiantes
def registro():
    while True:
        print("=================================")
        print("    Bienvenido al registro")
        print("=================================")
        print("1. Registrar estudiante")
        print("2. Mostrar lista de estudiantes")
        print("3. Eliminar estudiante")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            registrar_datos()
        elif opcion == "2":
            mostar_usuarios()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            print("Gracias por usar el sistema de registro...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
            continue

# Ejecutar la función principal del programa        
registro()
