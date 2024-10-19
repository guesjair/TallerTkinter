# Taller de Tkinter: Interfaces gráficas de novato a PRO
# En el aprendizaje de tkinter este archivo sería la lección #2
# Este es un formulario simple que muestra las base para capturar datos y mostrarlos
# en un messagebox, usando un par de funciones para tratar los datos del formulario

import tkinter as tk
from tkinter import messagebox

# Función para mostrar los datos capturados en el MessageBox por medio del formulario
def guardar_datos():
    id_alumno = entry_id_alumno.get()
    nombre_alumno = entry_nombre_alumno.get()
    calificacion = entry_calificacion.get()
    
    # Mostrar los datos capturados en un messagebox, tenemos el mismo formato de desplegadod de variables
    messagebox.showinfo("Datos Guardados", f"ID Alumno: {id_alumno}\nNombre Alumno: {nombre_alumno}\nCalificación: {calificacion}")

# Función para mostrar que los datos han sido actualizados
def actualizar_datos():
    messagebox.showinfo("Actualización", "Los datos han sido actualizados correctamente.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Alumnos")
ventana.geometry("400x300")  # Ancho y alto de la ventana
ventana.configure(bg="#f0f0f0")  # Fondo claro

# Etiqueta y entrada para ID Alumno
lbIdAlumno = tk.Label(ventana, text="ID Alumno:", font=("Tahoma", 12))
lbIdAlumno.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_id_alumno = tk.Entry(ventana)
entry_id_alumno.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y entrada para Nombre Alumno
lbAlumno = tk.Label(ventana, text="Nombre Alumno:", font=("Tahoma", 12))
lbAlumno.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_nombre_alumno = tk.Entry(ventana)
entry_nombre_alumno.grid(row=1, column=1, padx=10, pady=10)

# Etiqueta y entrada para Calificación
lbCalificacion = tk.Label(ventana, text="Calificación:", font=("Tahoma", 12))
lbCalificacion.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_calificacion = tk.Entry(ventana)
entry_calificacion.grid(row=2, column=1, padx=10, pady=10)

# Botón para Guardar los datos
btn_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
btn_guardar.grid(row=3, column=0, padx=10, pady=20)

# Botón para Actualizar los datos
btn_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_datos)
btn_actualizar.grid(row=3, column=1, padx=10, pady=20)

# Botón para Salir
btn_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
btn_salir.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Mantener la ventana en un ciclo
ventana.mainloop()
