from PIL import Image
import random
from images import *
import string


def create():
    # choice random images
    background = random.choices(backgrounds, weights=(50, 13, 37))[0]
    face = random.choices(faces, weights=(25, 17, 8, 17, 25, 8))[0]
    hat = random.choices(head_accessoires, weights=(37, 50, 13))[0]
    glass = random.choices(glasses, weights=(30, 15, 40, 15))[0]
    t_shirt = random.choices(t_shirts, weights=(35, 35, 8, 14, 8))[0]
    # open all images
    b = Image.open(background)
    f = Image.open(face)
    h = Image.open(hat)
    g = Image.open(glass)
    t = Image.open(t_shirt)
    # merge them in one
    b.paste(f, (0, 0), f)
    b.paste(g, (0, 0), g)
    b.paste(h, (0, 0), h)
    b.paste(t, (0, 0), t)
    # save with random name
    rname = "".join([random.choice(string.hexdigits[:16]) for x in range(32)])
    b.save(f"{rname}.png")


create()
