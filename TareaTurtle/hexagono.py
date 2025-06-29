import turtle

# Configurar turtle
t = turtle.Turtle()
t.speed(1)
t.shape("arrow")  # flecha visible

# Dibuja un hexágono regular (6 lados)
lado = 100
for _ in range(6):
    t.forward(lado)
    t.left(60)

t.hideturtle()
turtle.done()