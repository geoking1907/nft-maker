from PIL import Image
import random
from images import *
import string


def create():
    # choice random images
    background = random.choices(backgrounds, weights=(50, 13, 37))[0]
    face = random.choices(faces)[0]
    hat = random.choices(head_accessoires)[0]
    glass = random.choices(glasses)[0]
    t_shirt = random.choices(t_shirts)[0]
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
    b.show()


create()
