from turtle import *
size, gap = 80, 20
left(45)
for n in range(4):
    begin_fill()
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()
    penup()
    forward(size + gap); right(90); forward(size + gap); left(90)
    pendown()

done()