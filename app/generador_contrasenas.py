import random 
while True:
    try: 
        longitud = int(input("ingresa la longitud de la contrasena: "))

        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

        contrasena = ""

        for i in range(longitud):
         contrasena += random.choice(caracteres)
    
        print("tu contrasena es: " + contrasena)
        
        opcion = input("deseas generar otra contrasena? (s/n): ")
        
        if opcion.lower() == "s":
            continue
        elif opcion.lower() == "n":
            break
        else:
            print("opcion no valida, por favor ingresa 's' o 'n'.")
            continue
    except ValueError:
        print("por favor ingrese un valor valido.")