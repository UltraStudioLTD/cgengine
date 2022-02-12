#   MIT License
#
#   Copyright (c) 2021 tirimid
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

import random
import time
import os

from keyboard import is_pressed

# helper functions
def printsl(text):
    print(text, end = '')

def isKeyPressed(keyCode):
    return bool((is_pressed(keyCode)))

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
        return (point.x >= self.topLeft.x and point.x <= self.bottomRight.x) and (
            point.y >= self.topLeft.y and point.y <= self.bottomRight.y
        )

    def setOutlineChar(self, outlineChar):
        self.outlineChar = outlineChar

class ColliderRect:
    def __init__(self, topLeft, bottomRight):
        self.topLeft = topLeft
        self.bottomRight = bottomRight

    def isCollidingWith(self, other):
        return (
            self.bottomRight.x >= other.topLeft.x
            and self.topLeft.x <= other.bottomRight.x
        ) and (
            self.bottomRight.y >= other.topLeft.y
            and self.topLeft.y <= other.bottomRight.y
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

        cChar = ''

        for y in range(self.height):
            for x in range(self.width):
                cChar = self.bgChar

                for rect in self.rects:
                    if (rect.isPointWithin(Vec2(x, y))):
                        cChar = rect.char

                        if x in [rect.topLeft.x, rect.bottomRight.x]:
                            cChar = rect.outlineChar

                        if y in [rect.topLeft.y, rect.bottomRight.y]:
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
