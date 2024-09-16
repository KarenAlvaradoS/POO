import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


# Funciones para manejar eventos
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")


def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")


# Ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Frame para los campos de entrada
frame_inputs = tk.Frame(root)
frame_inputs.pack(padx=10, pady=10)

# Widgets para fecha, hora y descripción
tk.Label(frame_inputs, text="Fecha:").grid(row=0, column=0)
entry_fecha = DateEntry(frame_inputs)
entry_fecha.grid(row=0, column=1)

tk.Label(frame_inputs, text="Hora:").grid(row=1, column=0)
entry_hora = tk.Entry(frame_inputs)
entry_hora.grid(row=1, column=1)

tk.Label(frame_inputs, text="Descripción:").grid(row=2, column=0)
entry_desc = tk.Entry(frame_inputs)
entry_desc.grid(row=2, column=1)

# Frame para los botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=10)

# Botones
btn_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0)

btn_eliminar = tk.Button(frame_buttons, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1)

btn_salir = tk.Button(frame_buttons, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2)

# TreeView para mostrar los eventos
tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(padx=10, pady=10)

root.mainloop()
