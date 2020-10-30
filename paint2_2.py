"""Paint, for drawing shapes.
Exercises
1. Add a color. LISTO
2. Complete circle.
3. Complete rectangle. MEDIO LISTO
4. Complete triangle. LISTO
5. Add width parameter. LISTO
"""
#Librerias de importacion de datos especiales

from turtle import *
from freegames import vector

#Funcion para formar una linea dentro del programa usando dos taps

def line(start, end):
    "Draw line from start to end."
    pensize=10
    width(5)

    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Funcion para formar un cuadrado dentro del programa usando dos taps

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Funcion para formar un circulo dentro del programa

def circle(start, end):
    "Draw circle from start to end."
    pass  # TODO

#Funcion para formar un rectangulo dentro del programa

def rectangle(start, end):
    "Draw rectangle from start to end."
    fillcolor='red'
    up()
    begin_fill()
    goto(start.x,start.y)

    for count in range (2):
        forward(end.x - start.y)
        right(90)

        forward(end.y - start.x)
        right(90)

    down()
    end_fill()

#Funcion para formar un triangulo dentro del programa usando dos taps

def triangle(start,end):
    "Draw triangle from start to end."
    fillcolor='red'
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for count in range (2):
        forward(end.x - start.y)
        right(60)
    end_fill()

#Funcion para formar un trapecio dentro del programa usando dos taps

def trapecio(start, end):
    "Dibuja un trapecio from start to end."
    fillcolor="blue"
    up()
    goto(start.x,start.y)
    right(60)
    down()
    begin_fill()

    for count in range (3):
        forward(end.x - start.y)
        right(60)

    end_fill()

#Funcion para almacenar los datos de posicion de cada TAP

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}

setup(420, 420, 370, 0)
onscreenclick(tap)
#Codigo para cambiar el color del background del juego
bgcolor('Aquamarine')
listen()
onkey(undo, 'u')
#Formas de comunicar a traves de una letra
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'),'R')
onkey(lambda: color('light green'),'I')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', trapecio),'o')
done()