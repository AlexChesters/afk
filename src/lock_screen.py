from subprocess import call

def lock_screen():
    call(["open -a ScreenSaverEngine"], shell=True)
