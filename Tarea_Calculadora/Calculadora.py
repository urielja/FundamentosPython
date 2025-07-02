import tkinter as tk
import numexpr as ne #Libreria que evalua expresiones matematicas como cadenas de texto

class Calculadora:
    #Se crea una instancia de la clase y recibe root(ventana principal)
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")

        # Pantalla de resultados
        self.pantalla = tk.Entry(root, bg="gray", font=('Arial', 20), bd=10, relief=tk.FLAT, justify='right')
        self.pantalla.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Configurar filas y columnas para expandirse proporcionalmente
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            root.grid_columnconfigure(j, weight=1)

        # Se crea lista de botones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('CE', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('÷', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('x', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('+', 4, 2), ('-', 4, 3),
            ('=', 5, 1, 2)
        ]
        # Recorrer la lista de botones y colocar cada uno en la interfaz
        for b in botones:
            # Si el botón tiene 4 elementos, el último es colspan (cuántas columnas ocupa)
            if len(b) == 4:
                texto, fila, col, colspan = b
            else:
                # Si solo tiene 3, se asume colspan = 1
                texto, fila, col = b
                colspan = 1

            # Crear el botón
            btn = tk.Button(root,
                            text=texto,
                            font=('Arial', 18),
                            relief=tk.RAISED,
                            command=lambda t=texto: self.click(t))
            # Usa lambda para que al hacer clic se llame a self.click(texto)     
            # Colocar el botón en la cuadrícula
            btn.grid(row=fila, column=col, columnspan=colspan, sticky="nsew")

    def click(self, texto):
        if texto == '=':
            #Obtiene el texto de la pantalla (entry)
            try:
                expr = self.pantalla.get().replace('÷', '/') #reemplaza ÷ por /
                expr = self.pantalla.get().replace('x', '*') #reemplaza x por *
                resultado = str(ne.evaluate(expr)) # evalúa expresiones matemáticas escritas como cadenas de texto
                self.pantalla.delete(0, tk.END) 
                self.pantalla.insert(tk.END, resultado)
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(tk.END, "Error")
        elif texto == 'CE':
            actual = self.pantalla.get()
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(tk.END, actual[:-1])
        else:
            #Agrega el texto del botón al final de la pantalla
            self.pantalla.insert(tk.END, texto)

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()