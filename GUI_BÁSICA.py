import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_dato():
    dato = entrada_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_dato.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "El campo está vacío.")

# Función para limpiar la lista
def limpiar_datos():
    lista_datos.delete(0, tk.END)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta para el campo de texto
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=5)

# Campo de texto
entrada_dato = tk.Entry(ventana, width=40)
entrada_dato.pack(pady=5)

# Botón para agregar el dato
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
