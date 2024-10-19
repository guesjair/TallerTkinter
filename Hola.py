
# Hola mundo de forma gráfica en tkinter
# Revisamos aspectos generales de la creación de una pantalla de 400x200 
# Integrando algunos controles como botones, etiquetas y una función que despliega
# una messagebox.

# IMPORTANTE: Usamos para el acomodo de los controles el 

import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    lbResultado.config(text="Se guardo correctamente", fg="green")
    messagebox.showinfo("Información", "Se guardaron correctamente los datos")

# Creación de la ventana
ventana = tk.Tk()
ventana.title("Bienvenidos a Tkinter")
ventana.geometry("400x200")  # Ancho y alto
ventana.configure(bg="#f0f0f0")

# Creación de la etiqueta lbSaludo
lbSaludo = tk.Label(ventana, text="Hola Mundo Tkinter", font=("Tahoma", 12), fg="#0000FF")
lbSaludo.grid(row=0, column=0, padx=10, pady=10)  # Usar grid para la etiqueta

# Creación del botón Cerrar
btnCerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
btnCerrar.grid(row=3, column=0, padx=10, pady=10)  # Posicionarlo con grid

# Creación el botón Guardar
btnGuardar = tk.Button(ventana, text="Guardar", command=mostrar_mensaje)
btnGuardar.grid(row=1, column=1, padx=10, pady=10)  # Posicionarlo con grid

lbResultado = tk.Label(ventana, text="..", font=("Tahoma", 12), fg="#0000FF")
lbResultado.grid(row=5, column=0, padx=10, pady=10)  # Usar grid para la etiqueta


# Ciclo o loop para renderizar la ventana
ventana.mainloop()


#Apuntes:
# 1.- grid(): Coloca los widgets en una cuadrícula, especificando la fila y la columna donde quieres que aparezcan. En este caso, tanto el botón "Cerrar" como el botón "Guardar" se colocan en la fila 1 pero en columnas diferentes (column=0 para "Cerrar" y column=1 para "Guardar").
# 2.- padx y pady: Estos argumentos añaden espaciado alrededor del widget, tanto horizontal (padx) como vertical (pady), para evitar que los widgets estén demasiado juntos.

# Variantes de messagebox
# messagebox.showinfo()  Muestra un mensaje informátivo
# messagebox.showwarning  Muestra un mensaje de alerta
# messagebox.showerror  Muestra un mensaje de error
# messagebox.askquestion Muestra un mensaje de dialogo yes o no