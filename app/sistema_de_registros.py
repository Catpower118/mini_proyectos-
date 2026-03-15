# creacion de un sistema de registro de usuarios basico mediante funcines y una funcion padre
# tambien usando bucles while y manejo de errores try y except

# creacion del diccionario principal
datos = {}

# definimos la funcion agregar usuario
def usuario():
    while True:
        try:
            print("===================")
            print(" Nuevo usuario ")
            print("===================")
            
            nombre = input("Ingresa tu nombre: ")
            numero = int(input("Ingresa tu numero de telefono: "))
            contrasena = input("Ingresa una contrasena: ")
            
            datos[nombre] = {
                "numero": numero,
                "contrasena": contrasena
            }
            print("El usuario se ha guardado correctamente.")
            opcion = input("¿Desea añadir otro usuario? (s/n): ")
            if opcion.lower() == "s":
             continue
            else:
                print("gracias...")
                break
        except ValueError:
            print("Por favor ingresa un numero valido.")
            continue

# definimos la funcion ver usuarios         
def ver_usuario():
    while True:
        try:
            print("===============")
            print(" Ver usuarios ")
            print("===============")
            
            nombre_usuario = input("Ingresa el nombre del usuario: ")
            
            if nombre_usuario in datos:
                print(f"Nombre: {nombre_usuario}")
                print(f"Numero: {datos[nombre_usuario]['numero']}")
                print(f"Contrasena: {datos[nombre_usuario]['contrasena']}")
            else:
                print("El usuario no existe.")
                
                opcion = input("¿Desea ver otro usuario? (s/n): ")
                if opcion.lower() == "s":
                    continue
                else:
                    print("Gracias...")
                    break
        except ValueError:
            print("Por favor ingresa un nombre valido.")
            continue

# definimos la funcion eliminar usuario    
def eliminar_usuario():
    while True:
            print("======================")
            print(" Eliminar usuario ")
            print("======================")
            
            nombre_usuario = input("Ingresa el nombre del usuario: ")
            
            if nombre_usuario in datos:
                del datos[nombre_usuario]
                print("El usuario se ha eliminado correctamente.")
            else:
                print("El usuario no existe.")
                opcion = input("¿Desea eliminar otro usuario? (s/n): ")
                if opcion.lower() == "s":
                    continue
                else:
                    print("Gracias...")
                    break

        
        
# definimos la funcion padre que llamara a las otras funciones (hijas)      
def sistema():
    while True:
        try:
            print("========================")
            print(" Sistema de gestion ")
            print("========================")
            
            print("1. Añadir usuario")
            print("2. Ver usuario")
            print("3. Eliminar usuario")
            print("4. Salir")
            
            opcion = int(input("Selecciona una opcion: "))
            
            if opcion == 1:
                usuario()
            elif opcion == 2:
                ver_usuario()
            elif opcion == 3:
                eliminar_usuario()
            elif opcion == 4:
                print("Gracias...")
                break
            else:
                print("Opcion no valida.")
        except ValueError:
            print("Por favor ingresa una opcion valida.")
            continue
 
# ejecutamos la funcion principal        
sistema()

# mostramos todos los datos agregados al final del sistema
print("\nUsuarios registrados:")
print(datos)