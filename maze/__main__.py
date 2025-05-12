import sys
from window import Window

def main(*args, **kwargs):
    wind = Window(800, 600)
    wind.wait_for_close()

if __name__ == "__main__":
    main(sys.argv)