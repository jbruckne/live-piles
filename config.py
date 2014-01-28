from tiles import *

def addWeather(framework, x, y, w, h, bgcolor, textcolor):
    framework.tiles.append(WeatherTile(x, y, w, h, bgcolor, textcolor))
def addDateTime(framework, x, y, w, h, bgcolor, textcolor, formatstring, size):
    framework.tiles.append(DateTimeTile(x, y, w, h, bgcolor, textcolor, formatstring, size))
