import flet as ft          

class Miapp():
    def __init__(self):
        pass
    
    def main(self, page: ft.Page):
        page.title = "Mi aplicación con Flet"
        page.bgcolor = "black"
        page.window.height = 350
        page.window.width = 450
        page.window.max_height = 350
        page.window.max_width = 450
        page.window.min_height = 350
        page.window.min_width = 450
        page.window.center()
        page.window.resizable = False
        
        def Validar_usuario(e):
            if Entrada_Usuario.value == "paylug" and Entrada_Contraseña.value == "1234":
                etiqueta.content = ft.Text("Bienvenido, has iniciado sesion", color="green", size=20)
                page.update()
            else:
                etiqueta.content = ft.Text("Usuario o contraseña incorrectos", color="red", size=20)
                page.update()
        
        texto_1 = ft.Text("-------Usuario-------", color="green", size=20)
        Entrada_Usuario = ft.TextField(color="green", border_color="blue", cursor_color="white", width=200)
        Fila_Usuario = ft.Row(
            controls=[texto_1, Entrada_Usuario],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        page.add(Fila_Usuario)
        
        texto_2 = ft.Text("-------Contraseña-----", color="green", size=20)
        Entrada_Contraseña = ft.TextField(color="green", border_color="blue",
                                          cursor_color="white", width=200, password=True)
        Fila_Contraseña = ft.Row(
            controls=[texto_2, Entrada_Contraseña],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
        page.add(Fila_Contraseña)
        
        Boton_1 = ft.Button("Iniciar sesion", color="white", bgcolor="blue",
                            width=200, on_click=Validar_usuario)
        
        etiqueta = ft.Container(
            width=300,
            height=150,
            bgcolor="white",
            border_radius=10,
            padding=20,
            alignment=ft.Alignment.CENTER,
            content=ft.Text("Iniciar sesion", color="blue", size=20)
        )
        page.add(Boton_1, etiqueta)

miapp = Miapp()
ft.app(target=miapp.main)