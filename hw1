#############
# задание 1 #
#############

# напишите цикл, рисующий по
# вертикали фигуры (квадраты
# или другие из ссылки выше)

from drawbot_skia.drawbot import rect, saveImage, oval, fill, linearGradient
y=0
step = 180
# чтобы выполнить какую-либо инструкцию строго определенное число раз, воспользуемся функцией range()
for i in range(5):
    linearGradient(
    (100, 100),                         # startPoint
    (800, 800),                         # endPoint
    [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
    [0, .2, 1]                          # locations
    )
    oval(150, y, 150, 150)
    y=y+step
saveImage("задание 1.pdf")


#############
# задание 2 #
#############

# напишите вложенный (двойной)
# цикл, заполняющий холст фигурами
# полностью, по вертикали и
# горизонтали

from drawbot_skia.drawbot import rect, saveImage, oval, fill, linearGradient
x=0
y=0
step = 180
for i in range(10):
    for j in range(10):
        linearGradient(
        (100, 100),                         # startPoint
        (800, 800),                         # endPoint
        [(1, 0, 0), (0, 0, 1), (0, 1, 0)],  # colors
        [0, .2, 1]                          # locations
        )
        oval(x, y, 100, 100)
        y = y + step
    y = 0
    x = x + step
saveImage("задание 2.pdf")


##########################
# задание дополнительное #
# творческое, свободное  #
##########################

from drawbot_skia.drawbot import rect, saveImage, fill, size, newDrawing, polygon
newDrawing()
size(500,500)
step = 50
y = 200
width = 5

#ствол дерева
fill(0.6, 0.3, 0.2)
rect (145, 80, 10, 150)

#ветви
for i in range (3):
    fill(0.1, 0.8, 0.2)
    polygon((100-width,y), (200+width, y), (150, y+step), close=True)
    y -= step
    width += width
saveImage("задание 3.pdf")
