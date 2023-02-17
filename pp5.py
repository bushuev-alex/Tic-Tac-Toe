from p5 import *

def draw():
    # Sets the screen to be 640 pixels wide and 360 pixels high
    size(300, 300)

    # Set the background to black and turn off the fill color
    background(0)
    no_fill()

    # By default, the first parameter to rect() is the
    # coordinates of the upper-left corner and the second and third
    # parameter is the width and height
    stroke(255, 153, 0)
    line((0, height / 3), (width, height / 3))
    line((0, height * 2 / 3), (width, height * 2 / 3))
    line((width / 3, 0), (width / 3, height))
    line((width * 2 / 3, 0), (width * 2 / 3, height))


def mouse_clicked():
    return (mouse_x, mouse_y)


if __name__ == '__main__':
    run()