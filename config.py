from tiles import *

def addDateTime(framework, x, y, w, h, bgcolor, textcolor, formatstring, size):
    framework.tiles.append(DateTimeTile(x, y, w, h, bgcolor, textcolor, formatstring, size))
