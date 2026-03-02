# importamos la libreria tkinter
import tkinter as tk    

# definimos la funcion saludar usando Entrada.get() que nos permitira obtener la informacion
def saludar():
    texto = Entrada.get()
    Etiqueta_mensaje.config(text=f"Hola {texto}")

# creamos la ventana principal
ventana = tk.Tk()
ventana.title("SALUDAR")
ventana.geometry("350x300")
ventana.resizable(0,0)

# creamos la etiqueta para pedir nuestro nombre
etiqueta = tk.Label(ventana, text="Escribe tu nombre.")
etiqueta.pack(pady=5)

# creamos la entrada principal
Entrada = tk.Entry(ventana)
Entrada.pack(pady=5)

# creamos el boton
Boton = tk.Button(ventana, text="Saludar", command=saludar)
Boton.pack(pady=5)

# creamos la etiqueta para mostrar el mensaje
Etiqueta_mensaje = tk.Label(ventana, text="")
Etiqueta_mensaje.pack(pady=5)

# ejecutamos el bucle principal
ventana.mainloop()