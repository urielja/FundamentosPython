import turtle

def linea_punteada_con_flecha(t, longitud):
    for _ in range(int(longitud / 20)):
        t.pendown()
        t.forward(10)
        t.penup()
        t.forward(10)
    t.pendown()
    t.forward(5)  # último tramo para que la flecha quede más alineada
    t.shape("classic")
    t.stamp()

# Configuración
pantalla = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
t.penup()

# Primera flecha (más corta)
t.goto(-150, 50)
t.setheading(0)
linea_punteada_con_flecha(t, 120)

# Segunda flecha (más larga)
t.penup()
t.goto(-150, 0)
t.setheading(0)
linea_punteada_con_flecha(t, 200)

t.hideturtle()
pantalla.mainloop()