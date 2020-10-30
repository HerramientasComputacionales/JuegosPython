"""Paint, for drawing shapes.
Exercises
1. Add a color. LISTO
2. Complete circle.
3. Complete rectangle. MEDIO LISTO
4. Complete triangle. LISTO
5. Add width parameter. LISTO
"""
#Librerias de importacion de datos
from turtle import *
from freegames import vector

#Funcion especificamente para hacer una línea

def line(start, end):
    "Draw line from start to end."
    pensize=10
    width(5)

    up()
    goto(start.x, start.y)
    down()
    goto(end.x,end.y)

#Función para hacer un círculo
def circle(start, end):
    radio=(start.x , start.y)
    up()
    goto(start.x, start.y -radio)
    down()
    circle(radio)

#Funcion especificamente para hacer un rectangulo con relleno color rojo 

def rectangle(start, end):
    "Draw rectangle from start to end."

    fillcolor='red'
    up()
    goto(start.x,start.y)

    begin_fill()
    for count in range (2):
        forward(end.x - start.y)
        right(90)

        forward(end.y - start.x)
        right(90)


    end_fill()

#Funcion especificamente para hacer un cuadrado 

def square(start, end):
    up()
    goto(start.x , start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.y)
        left(90)
    end_fill()

#Funcion especificamente para hacer un triangulo

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

#Funcion especificamente para hacer un trapecio

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

#Funcion para resguardar los puntos donde se realizo un tap

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x,y)
    else:
        shape = state['shape']
        end = vector(x,y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    state[key] = value

state = {'start': None, 'shape': line}

setup(420, 420, 370, 0)
onscreenclick(tap)
#Seleccion de color de el fondo del juego
bgcolor('Aquamarine')
listen()
#Comandos utilizados por el usuario para llamar alguna de las funciones
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('red'),'R')
onkey(lambda: color('light green'),'I')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
onkey(lambda: store('shape', trapecio),'o')
done()
