import config

def setup(framework):
    config.addWeather(framework, 0, 3, 1, 1, (0, 0, 0), (255, 255, 255))
    config.addDateTime(framework, 0, 0, 2, 1, (0, 0, 0), (255, 255, 255), "%I:%M:%S%p", 1 / 4.5)
    config.addDateTime(framework, 0, 1, 2, 1, (0, 0, 0), (255, 255, 255), "%a %b %d, %Y", 1 / 6.0)
