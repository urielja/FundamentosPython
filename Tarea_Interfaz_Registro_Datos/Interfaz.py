from tkinter import *
from tkinter import ttk, messagebox
import csv
import os


def cancelar():
    root.destroy()

def guardar():
    datos = {
        "Nombre": entries[0].get(),
        "A. Paterno": entries[1].get(),
        "A. Materno": entries[2].get(),
        "Correo": entries[3].get(),
        "Móvil": entries[4].get(),
        "Estado laboral": estado_laboral.get(),
        "Estado": combo.get(),
    }

    # Capturar aficiones marcadas
    aficiones_seleccionadas = [k for k, v in aficiones_vars.items() if v.get() == 1]
    datos["Aficiones"] = ", ".join(aficiones_seleccionadas)

    # Guardar en CSV
    archivo = "datos_formulario.csv"
    # verifica si el archivo ya existe
    escribir_encabezados = not os.path.exists(archivo)
    #agrega datos sin borrar anteriores
    with open(archivo, mode="a", newline="", encoding="utf-8") as f:
        #con ditwriter escribe desde diccionarios
        writer = csv.DictWriter(f, fieldnames=datos.keys())
        #Si es la primera vez (archivo nuevo),
        # escribe la primera línea con los encabezados.
        if escribir_encabezados:
            writer.writeheader()
        #escribe una línea con los datos capturados.
        writer.writerow(datos)

    messagebox.showinfo("Éxito", "Datos guardados correctamente.")
    mostrar_datos_csv(archivo)

def mostrar_datos_csv(archivo):
    #Crea una ventana hija
    ventana = Toplevel(root)
    ventana.title("Datos Guardados")
    ventana.geometry("700x300")
    #se abre el archivo en modo lectura
    with open(archivo, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        filas = list(reader)
    #checa si hay filas de lo contrario lanza mensaje y detiene ejecucion
    if not filas:
        Label(ventana, text="No hay datos en el archivo").pack()
        return

    columnas = filas[0] #se guardan encabezados de CSV
    datos = filas[1:] #se guardan datos restantes

    #se crea en tabla que muestra datos en filas y columnas
    tree = ttk.Treeview(ventana, columns=columnas, show="headings")
    #Coloca treeview dentro de la ventana y lo expande
    tree.pack(fill=BOTH, expand=True)

    # Configurar encabezados
    for col in columnas:
        tree.heading(col, text=col)
        #Configura ancho y alineacion
        tree.column(col, width=100, anchor="center")

    # Agregar filas
    for fila in datos:
        #Se recorren todas las filas del CSV (excepto los encabezados).
        tree.insert("", "end", values=fila)


# Crear ventana principal
root = Tk()
root.title("Muestra Widgets")
root.geometry("500x400")

# Marco principal
frame_principal = Frame(root, bg="#EDE5DC")
frame_principal.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Submarco izquierdo (campos de texto)
frame_izquierdo = LabelFrame(frame_principal, bg="#EDE5DC")
frame_izquierdo.grid(row=0, column=0, padx=5, pady=5, sticky="n")

datos = ["Nombre:", "A. Paterno:", "A. Materno:", "Correo:", "Móvil:"]
estados=("Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
                                           "Chiapas", "Chihuahua", "CDMX", "Coahuila", "Colima", "Durango",
                                           "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco",
                                           "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla",
                                           "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora",
                                           "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas")
entries = []

for i, label_text in enumerate(datos):
    label = Label(frame_izquierdo, text=label_text, bg="#EDE5DC", anchor="w")
    label.grid(row=i, column=0, sticky="w", pady=2)
    entry = Entry(frame_izquierdo, width=30)
    entry.grid(row=i, column=1, pady=10)
    entries.append(entry)


# Submarco derecho (estado laboral)
frame_derecho = Frame(frame_principal, bg="#EDE5DC")
frame_derecho.grid(row=0, column=2, padx=10, sticky="e")

estado_laboral = StringVar()
estado_laboral.set("Estudiante")
for texto in ["Estudiante", "Empleado", "Desempleado"]:
    rb = Radiobutton(frame_derecho, text=texto, variable=estado_laboral, value=texto, bg="#EDE5DC")
    rb.pack(anchor="w")

# Aficiones
frame_aficiones = Frame(frame_principal, bg="#EDE5DC")
frame_aficiones = LabelFrame(frame_principal, text="Aficiones:", bg="#EDE5DC")
frame_aficiones.grid(row=2, column=0, padx=10, sticky="w")

aficiones_vars = {}
for i, aficion in enumerate(["Leer", "Música", "Videojuegos"]):
    var = IntVar()
    chk = Checkbutton(frame_aficiones, text=aficion, variable=var, bg="#EDE5DC")
    chk.grid(row=0, column=i, padx=5)
    aficiones_vars[aficion] = var

# ComboBox de estados
frame_combobox = Frame(frame_principal, bg="#EDE5DC")
frame_combobox.grid(row=3, column=2, sticky="e", pady=10)

combo =  ttk.Combobox(frame_combobox, textvariable=estados,  state="readonly")
combo.set("Estados (32)")
combo.grid()
combo['values'] = estados

# Botones
frame_botones = Frame(frame_principal, bg="#EDE5DC")
frame_botones.grid(row=3, column=0, sticky="ws", pady=10)

btn_guardar = Button(frame_botones, text="Guardar",command= guardar, width=10)
btn_guardar.grid(row=3, column=0, padx=10)

btn_cancelar = Button(frame_botones, text="Cancelar",command=cancelar, width=10)
btn_cancelar.grid(row=3, column=1, padx=10)

# Ejecutar aplicación
root.mainloop()