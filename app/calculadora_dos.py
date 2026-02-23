def suma():
    while True:
     try:
        num1 = float(input("ingresa el primer numero: "))
        num2 = float(input("ingresa el segundo numero: "))
        resutado = num1 + num2
        print(resutado)
        opcion = input("deseas continuar? (s/n): ")
        if opcion.lower() == "s":
            continue
        else:
            break
     except ValueError:
       print("por favor ingresa datos validos.")
       
def resta():
    while True:
     try:
        num1 = float(input("ingresa el primer numero: "))
        num2 = float(input("ingresa el segundo numero: "))
        resutado = num1 - num2
        print(resutado)
        opcion = input("deseas continuar? (s/n): ")
        if opcion.lower() == "s":
            continue
        else:
            break
     except ValueError:
       print("por favor ingresa datos validos.")
       
def multiplicacion():
    while True:
     try:
        num1 = float(input("ingresa el primer numero: "))
        num2 = float(input("ingresa el segundo numero: "))
        resutado = num1 * num2
        print(resutado)
        opcion = input("deseas continuar? (s/n): ")
        if opcion.lower() == "s":
            continue
        else:
            break
     except ValueError:
       print("por favor ingresa datos validos.")
       
def division():
    while True:
     try:
        num1 = float(input("ingresa el primer numero: "))
        num2 = float(input("ingresa el segundo numero: "))
        if num2 == 0:
         print("no se puede dividir entre cero.")
        else:
         resutado = num1 / num2
         print(round(resutado, 2))
        opcion = input("deseas continuar? (s/n): ")
        if opcion.lower() == "s":
            continue
        else:
            break
     except ValueError:
       print("por favor ingresa datos validos.")
       
def calculadora():
    while True:
        print("=====================")
        print("   CALCULADORA    ")
        print("=====================")
        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division")
        print("5. salir")
        try:
            opcion = int(input("selecione una opcion valida: "))
            if opcion == 1:
                suma()
            elif opcion == 2:
                resta()
            elif opcion == 3:
                multiplicacion()
            elif opcion == 4:
                division()
            elif opcion == 5:
                break
            else:
                print("opcion invalida")
                continue
        except ValueError:
            print("por favor ingresa un numero valido.")
            
calculadora()

# esta calculadora se hace mediante funciones cada funcion tiene su propia operacion
# y todas estan vinculadas a una funcion padre que es la que se ejecuta al iniciar el programa 
# y manda a llamar a las funciones hijas dependediendo de la opcion del usuario
# este miniprograma se puede simplificar eliminado las funciones hijas y poniendo condicionales

       