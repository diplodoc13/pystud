import turtle as t
from math import ceil
from random import randrange

t.ht()
angle = float(input('Angle: '))
radius = float(input('Radius: '))
size = ceil(360 / angle)
end = randrange(16777216)
step = randrange(-200, 200)
t.speed(0)
for i in range(size):
    t.color(hex(end - i * step).replace('0x', '#'))
    t.circle(radius)
    t.lt(angle)
    if not i % step:
        end = randrange(16777216)
        step = randrange(-200, 200)