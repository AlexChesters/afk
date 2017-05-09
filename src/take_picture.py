from subprocess import call
from os import devnull

DEVNULL = open(devnull, 'w')
IMAGE_PATH = "image.png"

def take_picture():
    call(["imagesnap", "-w", "1", IMAGE_PATH], stdout=DEVNULL)
    return IMAGE_PATH
