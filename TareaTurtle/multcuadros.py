import turtle

# Configurar ventana
turtle.bgcolor("white")
t = turtle.Turtle()
t.speed(0)  # Máxima velocidad

# Dibujo de rombos rotados
for _ in range(5):
    for _ in range(4):
        t.forward(100)
        t.left(90)
    t.left(20)  # Rotación para el siguiente cuadrado

turtle.done()