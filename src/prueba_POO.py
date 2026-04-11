class Calculadora():
    def __init__(self):
        pass

    def sumar(self):
        while True:
            try:
                print(">>> SUMA <<<")
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                print("Rsultado:", round(num1 + num2, 2))
                opcion = input("¿Desea realizar otra operación? (s/n): ")
                if opcion.lower() == 's':
                    continue
                else:
                    print("Saliendo de la calculadora...")
                    break
            except ValueError:
                print("Error: Por favor, ingrese números válidos.")
    
    def restar(self):
        while True:
            try:
                print(">>> RESTA <<<")
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                print("Resultado:", round(num1 - num2, 2))
                opcion = input("¿Desea realizar otra operación? (s/n): ")
                if opcion.lower() == 's':
                    continue
                else:
                    print("Saliendo de la calculadora...")
                    break
            except ValueError:
                print("Error: Por favor, ingrese números válidos.")
    
    def multiplicar(self):
        while True:
            try:
                print(">>> MULTIPLICACIÓN <<<")
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                print("Resultado:", round(num1 * num2, 2))
                opcion = input("¿Desea realizar otra operación? (s/n): ")
                if opcion.lower() == 's':
                    continue
                else:
                    print("Saliendo de la calculadora...")
                    break
            except ValueError:
                print("Error: Por favor, ingrese números válidos.")
    
    def dividir(self):
        while True:
            try:
                print(">>> DIVISIÓN <<<")
                num1 = float(input("Ingrese el primer numero: "))
                num2 = float(input("Ingrese el segundo numero: "))
                if num2 == 0:
                    print("Error: No se puede dividir por cero.")
                    continue
                else:
                    print("Resultado:", round(num1 / num2, 2))
                    
                opcion = input("¿Desea realizar otra operación? (s/n): ")
                if opcion.lower() == 's':
                    continue
                else:
                    print("Saliendo de la calculadora...")
                    break
            except ValueError:
                print("Error: Por favor, ingrese números válidos.")
        
class MiCalculadora():
    def __init__(self):
        self.calculadora = Calculadora()
        
    def Mostrar_menu(self):
        print(">>> BIENVENIDO A LA CALCULADORA <<<")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
    def Ejecutar_op(self):
        while True:
            try:
                self.Mostrar_menu()
                opcion = input("Seleccione una opción (1-5): ")
                
                if opcion == "1":
                    self.calculadora.sumar()
                elif opcion == "2":
                    self.calculadora.restar()
                elif opcion == "3":
                    self.calculadora.multiplicar()
                elif opcion == "4":
                    self.calculadora.dividir()
                elif opcion == "5":
                    print("Saliendo de la calculadora...")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
            except ValueError:
                print("Error: Por favor, ingrese números válidos.")
            
mi_calculadora = MiCalculadora()
mi_calculadora.Ejecutar_op()