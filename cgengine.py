import random
from time import sleep
from sys import stdin, stdout

try:
    from msvcrt import getch, khbit
except:
    from termios import 
    def getch(echo: bool = False) -> str:
        

class Vector:
    def __init__(self, x, y) -> None:
        self.X = x
        self.Y = y
        self.Z = z


class RenderRect:
    def __init__(self, topLeft, bottomRight, char):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.char = char
        self.outlineChar = char

    def isPointWithin(self, point):
        return (point.X >= self.topLeft.X and point.X <= self.bottomRight.X) and (
            point.Y >= self.topLeft.Y and point.Y <= self.bottomRight.Y
        )

    def setOutlineChar(self, outlineChar):
        self.outlineChar = outlineChar


class ColliderRect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def isCollidingWith(self, other):
        return (
            self.bottomRight.X >= other.topLeft.X
            and self.topLeft.X <= other.bottomRight.X
        ) and (
            self.bottomRight.Y >= other.topLeft.Y
            and self.topLeft.Y <= other.bottomRight.Y
        )


# game infrastructure
class Game:
    def __init__(self, gameMan):
        self.gameMan = gameMan

    def update(self):
        self.gameMan.update()


class GameManager:
    def __init__(self, drawMan):
        self.drawMan = drawMan

    def update(self):
        self.drawMan.present()


class DrawManager:
    def __init__(self, width, height, bgChar):
        self.width = width
        self.height = height
        self.bgChar = bgChar
        self.rects = []

    def registerRect(self, rect):
        self.rects.append(rect)

    # can be used for registering rects which update frequently
    def registerRectId(self, rect, index):
        self.rects.insert(index, rect)

    def unregisterRect(self, index):
        self.rects.pop(index)

    def present(self):
        countX = 0
        countY = 0

        cChar = ""

        for y in range(self.height):
            for x in range(self.width):
                cChar = self.bgChar

                for rect in self.rects:
                    if rect.isPointWithin(Vector(x, y)):
                        cChar = rect.char

                        if x in [rect.topLeft.X, rect.bottomRight.X]:
                            cChar = rect.outlineChar

                        if y in [rect.topLeft.Y, rect.bottomRight.Y]:
                            cChar = rect.outlineChar

                printsl(cChar)

                countX += 1

                if countX >= self.width:
                    countX = 0
                    printsl("\n")

            countY += 1

            if countY >= self.height:
                countY = 0
                printsl("\n")
