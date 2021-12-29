from PIL import Image
import random
from images import *

backgrounds = [
    'b/b1.png',
    'b/b2.png',
    'b/b3.png'
]
faces = [
    'f/f1.png',
    'f/f2.png',
    'f/f3.png',
    'f/f4.png',
    'f/f5.png',
    'f/f6.png'
]
head_accessoires = [
    'h/h1.png',
    'h/h2.png',
    'h/h3.png'
]
glasses = [
    'g/g1.png',
    'g/g2.png',
    'g/g3.png',
    'g/g4.png'
]
t_shirts = [
    't/t1.png',
    't/t2.png',
    't/t3.png',
    't/t4.png',
    't/t5.png'
]


def create():
    background = random.choices(backgrounds, weights=(50, 13, 37))[0]
    face = random.choices(faces, weights=(25, 17, 8, 17, 25, 8))[0]
    hat = random.choices(head_accessoires, weights=(37, 50, 13))[0]
    glass = random.choices(glasses, weights=(30, 15, 40, 15))[0]
    t_shirt = random.choices(t_shirts, weights=(35, 35, 8, 14, 8))[0]

    b = Image.open(background)
    f = Image.open(face)
    h = Image.open(hat)
    g = Image.open(glass)
    t = Image.open(t_shirt)

    b.paste(f, (0, 0), f)
    b.paste(g, (0, 0), g)
    b.paste(h, (0, 0), h)
    b.paste(t, (0, 0), t)

    b.show()


create()
create()
create()
create()
create()
