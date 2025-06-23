from tkinter import *
from tkinter import ttk

raiz = Tk()

etqText = ttk.Label(raiz, text="Etiqueta solo texto")
etqText.grid()

imagen = PhotoImage(file="mario.png")

etqImagen = ttk.Label(raiz)
etqImagen.grid()
etqImagen['image'] = imagen

etqCombinada = ttk.Label(raiz, text="EtqCombinada", compound="center")
etqCombinada.grid()
etqCombinada['image'] = imagen

raiz.mainloop()