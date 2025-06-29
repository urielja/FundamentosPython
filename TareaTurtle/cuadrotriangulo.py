import turtle

t = turtle.Turtle()
t.speed(1)
t.shape("arrow")  # mostrar la flecha como en la imagen

# Lado del cuadrado
lado = 100

# Dibujar el cuadrado
for _ in range(4):
    t.forward(lado)
    t.left(90)

# Dibujar la primera diagonal: inferior izquierda a superior derecha
t.goto(lado, lado)

# Dibujar la segunda diagonal: superior izquierda a inferior derecha
t.penup()
t.goto(0, lado)
t.pendown()
t.goto(lado, 0)

# Línea horizontal en la parte superior del cuadrado
t.penup()
t.goto(0, lado)
t.pendown()
t.goto(lado, lado)

# Dibujar el techo (triángulo)
t.goto(lado / 2, lado + (lado / 2))  # pico superior del triángulo
t.goto(0, lado)  # cerrar el triángulo

t.hideturtle()
turtle.done()