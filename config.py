from tiles import *

def addClock(framework, x, y, w, h, bgcolor, textcolor):
    framework.tiles.append(ClockTile(x, y, w, h, bgcolor, textcolor))
