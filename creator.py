from PIL import Image
import random
from images import *

backgrounds = [
    'images/b/b1.png',
    'images/b/b2.png',
    'images/b/b3.png'
]
faces = [
    'images/f/f1.png',
    'images/f/f2.png',
    'images/f/f3.png',
    'images/f/f4.png',
    'images/f/f5.png',
    'images/f/f6.png'
]
head_accessoires = [
    'images/h/h1.png',
    'images/h/h2.png',
    'images/h/h3.png'
]
glasses = [
    'images/g/g1.png',
    'images/g/g2.png',
    'images/g/g3.png',
    'images/g/g4.png'
]
t_shirts = [
    'images/t/t1.png',
    'images/t/t2.png',
    'images/t/t3.png',
    'images/t/t4.png',
    'images/t/t5.png'
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
