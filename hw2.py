#############
# задание 1 #
#############

# перепешите последний пример
# так, чтобы в нём появилась
# обработка правила "2",
# рисующая контурный круг

# подсказки:
# пустая заливка — fill(None)
# цвет обводки — stroke(0, 0, 0)
# толщина — strokeWidth(3)

from drawbot_skia.drawbot import rect, oval, newPage, saveImage, fill, stroke, strokeWidth, newDrawing
rules = [1, 0, 1, 0, 2, 0, 1, "сибаину"] * 20
w, h = 742.5, 1050
newPage(w, h)
margin=80
x = margin
y = h - margin
step = (w - margin * 2) / 6
size = step

for rule in rules:
    # круг, если правило == 0
    if rule == 0:
        fill(0)
        oval(x, y - step, size, size)
    # квадрат, если правило == 1
    elif rule == 1:
        fill(0)
        rect(x, y - step, size, size)
    elif rule == 2:
        fill(None)
        stroke(0, 0, 0)
        strokeWidth(3)
        oval (x, y - step, size, size)
     # всё другое print в консоль
    else:
        print(rule, "<— неизвестное правило")
    x += step
    if x >= w - margin:
        x = margin
        y -= step
    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin
saveImage("задание1_04.12.pdf")


#############
# задание 2 #
#############

from drawbot_skia.drawbot import rect, oval, newPage, saveImage, fill, stroke, strokeWidth, newDrawing
rules = [0, 1, 2, 0, 1, 2, "сибаину"] * 20
w, h = 742.5, 1050
newPage(w, h)
margin=80
x = margin
y = h - margin
step = (w - margin * 2) / 10
size = step

for rule in rules:
    # круг, если правило == 0
    if rule == 0:
        fill(1, 0.5, 0)
        stroke(0, 0, 0.5)
        strokeWidth(3)
        oval(x, y - step, size, size)
    # квадрат, если правило == 1
    elif rule == 1:
        fill(0.5)
        stroke(1, 0, 0)
        strokeWidth(3)
        rect(x, y - step, size, size)
    elif rule == 2:
        fill(None)
        stroke(0, 0, 1)
        strokeWidth(3)
        oval (x, y - step, size, size)
     # всё другое print в консоль
    else:
        print(rule, "<— неизвестное правило")
    x += step
    if x >= w - margin:
        x = margin
        y -= step
    if y - step < margin:
        newPage(w, h)
        x = margin
        y = h - margin
saveImage("задание2_04.12.pdf")
