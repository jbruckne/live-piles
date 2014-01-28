import config

def setup(framework):
    config.addClock(framework, 0, 0, 2, 1, (0, 0, 0), (255, 255, 255))
    config.addDate(framework, 0, 1, 2, 1, (0, 0, 0), (255, 255, 255))
