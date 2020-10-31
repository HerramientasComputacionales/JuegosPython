"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits. LISTO
2. Vary the effect of gravity. LISTO
3. Apply gravity to the targets. LISTO
4. Change the speed of the ball. LISTO

"""
#Porgrama  documentado 

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)		#vector de velocidad
targets = []
Hit = 0				#contador de impactos 

def tap(x, y):			#esta  funcion nos srive para ver la direcccion en la que va la pelota
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10

def inside(xy):			#Mando si  esta dentro de la pantalla
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():			#Muestra en pantalla lo targets y la bola resuktante del tab
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    global Hit
    "Move ball and targets."
    if randrange(40) == 0:			#delimitamos los movimientos de los targets
        y = randrange(-150, 150)		# se  eligio un rango en  y 
        target = vector(200, y)
        targets.append(target)

    for target in targets:			#ajusta la dereccion en x  y en y de target
        target.x -= 0.50
        target.y -= 9.81*0.001

    if inside(ball):				# curvatura  que lleva el proyectil 
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:				#cuando aun no le pega el proyectil a los targets se hace una comprobación
        if abs(target - ball) > 13:
            targets.append(target)
        else:					#contador de impactos que se va sumando 
            Hit=Hit+1
            print(Hit)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 50)

#main donde se llaman a  las funciones 
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
