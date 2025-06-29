import turtle

def dibujar_poligono(t, lados, longitud):
    angulo = 360 / lados
    for _ in range(lados):
        t.forward(longitud)
        t.left(angulo)

# Configurar turtle
t = turtle.Turtle()
t.speed(1)

# Dibujar triángulo
t.penup()
t.goto(-200, 0)
t.pendown()
dibujar_poligono(t, 3, 60)

# Dibujar cuadrado
t.penup()
t.goto(-80, 0)
t.pendown()
dibujar_poligono(t, 4, 60)

# Dibujar pentágono
t.penup()
t.goto(60, 0)
t.pendown()
dibujar_poligono(t, 5, 60)

t.hideturtle()
turtle.done()