"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

#La comida aparece exactamente en el centro
# por lo tanto las coordenadas son  (0,0), si
# se modifican las coordenadas, cambiara la fruta.
# Nota: Utilizar multiplos del 10.
food = vector(20, 20)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
#Se coloco un if para diferennciar el choque del cuerpo
#con el choque de una pared.
#En esta area se debe modificar para los contornos

        if head in snake:
                square(head.x, head.y, 9, 'red')
                update()
                return
        else:
               if head.x == 190:
                       head.x = -200
                       update()
               elif head.x == -200:
                       head.x = 190
                       update()
               elif head.y == 190:
                       head.y = -200
                       update()
               elif head.y == -200:
                       head.y = 190
                       update()
#Se elimino el return, de esta manera no se termina el juego
#Al momento de llegar a los contornos.


    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
#Para aumentar la velocidad de Snake, el contador tiene que ser menor, para mas lento, mayor
#El valor original es 100
    ontimer(move, 60)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
#En este caso, Snake ya responde a las flechas, no obstante
#Para cambiar las direcciones, vasta con modificar las teclas
#que se encuentran entre comillas.
#Valores originales: Right, Left, Up, Down, respectivamente
onkey(lambda: change(10, 0), 'd')
onkey(lambda: change(-10, 0), 'a')
onkey(lambda: change(0, 10), 'w')
onkey(lambda: change(0, -10), 's')
move()
done()
