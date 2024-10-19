import tkinter as tk
from tkinter import messagebox  # Importar messagebox

# Función que se ejecutará al hacer clic en el botón Guardar
def mostrar_mensaje():
    lblMensaje.config(text="Se guardó correctamente desde una función", fg="green")
    messagebox.showinfo("Información", "Se guardó correctamente desde una función")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Bienvenidos a Tkinter")
ventana.geometry("400x200")  # Ancho y alto
ventana.configure(bg="#f0f0f0")

# Crear la etiqueta de saludo
lbSaludo = tk.Label(ventana, text="Hola Mundo Tkinter", font=("Tahoma", 12), fg="#0000FF")
lbSaludo.grid(row=0, column=0, padx=10, pady=10)  # Usar grid para la etiqueta

# Crear el botón Cerrar
btnCerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
btnCerrar.grid(row=1, column=0, padx=10, pady=10)  # Posicionarlo con grid

# Crear el botón Guardar
btnGuardar = tk.Button(ventana, text="Guardar", command=mostrar_mensaje)
btnGuardar.grid(row=1, column=1, padx=10, pady=10)  # Posicionarlo con grid

# Crear una etiqueta para mostrar el mensaje
lblMensaje = tk.Label(ventana, text="", font=("Tahoma", 10))
lblMensaje.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Mantener el ciclo o loop para renderizar la ventana
ventana.mainloop()


Variantes de messagebox:
messagebox.showinfo(): Muestra un mensaje informativo.
messagebox.showwarning(): Muestra una advertencia.
messagebox.showerror(): Muestra un error.
messagebox.askquestion(): Muestra un cuadro de diálogo con una pregunta y devuelve 'yes' o 'no'.