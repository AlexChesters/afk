from subprocess import call
from os import devnull

DEVNULL = open(devnull, 'w')

def take_picture():
    call(["imagesnap", "-w", "1", "image.png"], stdout=DEVNULL)
    return 'image.png'
