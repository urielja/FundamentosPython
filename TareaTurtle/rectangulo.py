import turtle

# Configurar la pantalla
screen = turtle.Screen()
screen.bgcolor("white")  # Color de fondo

# Crear un objeto turtle
t = turtle.Turtle()

# Establecer la velocidad del dibujo
t.speed(2)

# Dibujar un rectángulo
for _ in range(2):
    t.forward(200)  # Mover hacia adelante 200 unidades
    t.left(90)      # Girar 90 grados a la izquierda
    t.forward(100)  # Mover hacia adelante 100 unidades
    t.left(90)      # Girar 90 grados a la izquierda

# Finalizar
turtle.done()