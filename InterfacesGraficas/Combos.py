from tkinter import *
from tkinter import ttk 

estados = ("Michoacan","SLP","CDMX", "Jalisco","Queretaro", "Nayarit","Colima")

raiz = Tk()

estado = StringVar()

comboEstados = ttk.Combobox(raiz, textvariable=estado)
comboEstados.grid()
comboEstados['values'] = estados

raiz.mainloop()



