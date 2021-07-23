import random
import time
import os

from keyboard import is_pressed

# helper functions
def printsl(text):
    print(text, end = '')

def isKeyPressed(keyCode):
    if (is_pressed(keyCode)):
        return True

    return False

def sleeps(seconds):
    time.sleep(seconds)

def clearScreen():
    os.system("cls")

# types
class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class RenderRect:
    def __init__(self, topLeft, bottomRight, char):
        self.topLeft = topLeft
        self.bottomRight = bottomRight
        self.char = char
        self.outlineChar = char

    def isPointWithin(self, point):
        if (point.x >= self.topLeft.x and point.x <= self.bottomRight.x):
            if (point.y >= self.topLeft.y and point.y <= self.bottomRight.y):
                return True

        return False

    def setOutlineChar(self, outlineChar):
        self.outlineChar = outlineChar

class ColliderRect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def isCollidingWith(self, other):
        if (self.bottomRight.x >= other.topLeft.x and self.topLeft.x <= other.bottomRight.x):
            if (self.bottomRight.y >= other.topLeft.y and self.topLeft.y <= other.bottomRight.y):
                return True

        return False

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

        cChar = ''

        for y in range(self.height):
            for x in range(self.width):
                cChar = self.bgChar

                for rect in self.rects:
                    if (rect.isPointWithin(Vec2(x, y))):
                        cChar = rect.char

                        if (x == rect.topLeft.x or x == rect.bottomRight.x):
                            cChar = rect.outlineChar

                        if (y == rect.topLeft.y or y == rect.bottomRight.y):
                            cChar = rect.outlineChar

                printsl(cChar)

                countX += 1

                if (countX >= self.width):
                    countX = 0
                    printsl('\n')

            countY += 1

            if (countY >= self.height):
                countY = 0
                printsl('\n')
