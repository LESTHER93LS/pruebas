import turtle
import random
from random import randint
from turtle import*
#dibujo de la pista
penup()
goto(-280, 170)
pendown()
for paso in range(6):
    write(paso, align='center')
    right(90)
    forward(0)
    pendown()
    for _ in range(6):
        forward(30)
        penup()
        forward(50)
        pendown()
    penup()
    backward(480)
    left(90)
    forward(100)
    speed(100)


# Configuración inicial de la ventana
ventana = turtle.Screen()
ventana.setup(720, 600)

# Línea de inicio
linea_inicio = turtle.Turtle()
linea_inicio.penup()
linea_inicio.goto(-280, 170)
linea_inicio.pendown()
linea_inicio.goto(-280, -260)

# Línea de meta
linea_meta = turtle.Turtle()
linea_meta.penup()
linea_meta.goto(280, 170)
linea_meta.pendown()
linea_meta.goto(280, -260)
#lineas verticales de la pista


# Tortugas
tortugas = []
colores = ["red", "orange", "blue", "green", "purple"]
for i in range(5):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(colores[i])
    tortuga.penup()
    tortuga.goto(-320, 150 - i * 100)
    tortuga.pendown()
    tortugas.append(tortuga)
# Función para avanzar las tortugas
def avanzar():
    ganador = None
    for tortuga in tortugas:
        if ganador is None:
            # Avanzar la tortuga de forma aleatoria
            avance = random.randint(1, 20)
            tortuga.forward(avance)

            # Verificar si la tortuga ha llegado a la meta
            if tortuga.xcor() >= 250:
                ganador = tortuga
                color_original = ganador.color()[0]
                ganador.color("black")

                for i in range(10):
                    ganador.forward(5)
                    ganador.backward(5)
                ganador.color(color_original)
        else:
            "ni modo"
    if ganador is None:
        # Programar la siguiente llamada a la función avanzar
        ventana.ontimer(avanzar, 100)


ventana.onkeypress(avanzar, "space")
ventana.listen()
turtle.mainloop()