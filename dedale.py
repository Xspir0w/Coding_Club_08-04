from tkinter import *


incr = 2
size = incr * 10
posX = 1
posY = 1
map = [[]] * 100


for value in range(0, 100):
    map[value] = [0] * 100



def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x * (incr), 0, x * (incr), canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y * (incr), canvas_width, y * (incr), fill="#476042")


def right():
    global posX
    global posY
    if (map[posY][posX + 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)


def left():
    global posX
    global posY
    if (map[posY][posX - 1] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posX -= 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)


def up():
    global posY
    global posX
    if (map[posY - 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY -= 1

    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)


def down():
    global posY
    global posX
    if (map[posY + 1][posX] == 1):
        return
    setACaseXY(posX, posY, 'grey')
    map[posY][posX] = -1
    posY += 1
    setACaseXY(posX, posY, 'yellow')
    if (map[posY][posX] == 2):
        exit(0)



dir = []
last_moove = "down"
def algo(value):
    global last_moove
    if (last_moove=="down"):
        if (map[posY][posX - 1] == 1) and not (map[posY + 1][posX] == 1):
            down()

        elif (map[posY][posX - 1] == 1) and (map[posY][posX + 1] == 1) and (map[posY + 1][posX] == 1):
            up()
            last_moove="up"

        elif (map[posY][posX - 1] == 1) and (map[posY + 1][posX] == 1):
            right()
            last_moove="right"

        elif (map[posY][posX - 1] != 1) :
            left()
            last_moove="left"



    elif (last_moove=="up"):

        if (map[posY][posX + 1] == 1) and not (map[posY - 1][posX] == 1):
            up()

        elif (map[posY][posX - 1] == 1) and (map[posY][posX + 1] == 1) and (map[posY - 1][posX] == 1):
            down()
            prevDirection="down"

        elif (map[posY][posX + 1] == 1) and (map[posY - 1][posX] == 1):
            left()
            last_moove="left"

        elif (map[posY][posX + 1] != 1):
            right()
            last_moove="right"




    elif (last_moove=="right"):
        if (map[posY + 1][posX] == 1) and not (map[posY][posX + 1] == 1):
            right()

        elif (map[posY - 1][posX] == 1) and (map[posY][posX + 1] == 1) and (map[posY + 1][posX] == 1):
            left()
            last_moove="left"

        elif (map[posY + 1][posX] == 1) and (map[posY][posX + 1] == 1):
            up()
            last_moove="up"

        elif (map[posY + 1][posX] != 1):
            down()
            last_moove="down"




    elif (last_moove=="left"):
        if (map[posY - 1][posX] == 1) and not (map[posY][posX - 1] == 1):
            left()

        elif (map[posY][posX - 1] == 1) and (map[posY - 1][posX] == 1) and (map[posY + 1][posX] == 1):
            right()
            last_moove="right"

        elif (map[posY - 1][posX] == 1) and (map[posY][posX - 1] == 1):
            down()
            last_moove="down"

        elif (map[posY - 1][posX] != 1):
            up()
            last_moove="up"




    else:
        down()











def setACaseXY(X, Y, color):
    points = [X * size, Y * size, size * (X + 1), Y * size, size * (X + 1), size * (Y + 1), X * size, size * (Y + 1)]
    w.create_polygon(points, outline="#476042", fill=color, width=4)



master = Tk()
canvas_width = 1300
canvas_height = 1000
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)











path = 'map.txt'
with open(path) as fp:
   line = fp.readline()
   cnt = 0
   while line:
       x = line.find('x')
       while x != -1:
           setACaseXY(x, cnt, 'red')
           map[cnt][x] = 1
           x = line.find('x', x + 1)
       line = fp.readline()
       cnt += 1

w.pack()

setACaseXY(47, 21, 'green')
map[21][47] = 2


for value in range(0, 1000):
    master.after(value * 35, algo, value)

checkered(w,10)

mainloop()
