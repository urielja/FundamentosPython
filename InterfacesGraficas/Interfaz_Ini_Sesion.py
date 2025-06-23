from tkinter import *
from tkinter import ttk

def ini_sesion(*args):
    try:
        pass
    except ValueError:
        pass

raiz = Tk() # Se crea la ventana
raiz.title("Inicio de sesion") # se agrega el texto

marcoPrincipal = ttk.Frame(raiz, padding="3 3 12 12")
marcoPrincipal.grid(column=0, row=0, sticky=(N, W, E, S))
marcoPrincipal.columnconfigure(0,weight=1)
marcoPrincipal.rowconfigure(0, weight=1)

usuario = StringVar()
contrasena = StringVar()

# Etiquetas y campos de texto
ttk.Label(marcoPrincipal, text="Usuario:").grid(column=1, row=1, sticky=E)
usuario = ttk.Entry(marcoPrincipal, width=15, textvariable=usuario)
usuario.grid(column=2, row=1, sticky=(W, E))

ttk.Label(marcoPrincipal, text="Contraseña:").grid(column=1, row=2, sticky=E)
contrasena = ttk.Entry(marcoPrincipal, width=15, textvariable=contrasena)
contrasena.grid(column=2, row=2, sticky=(W, E))

ttk.Button(marcoPrincipal, text="Ingresar").grid(column=2, row=3, sticky=E)

for child in marcoPrincipal.winfo_children():
    child.grid_configure(padx=5, pady=5)

usuario.focus()
contrasena.focus()
raiz.mainloop()