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

from cgengine import *

# construct the game and managers
drawMan = DrawManager(110, 28, '.')
gameMan = GameManager(drawMan)
game = Game(gameMan)

rr = RenderRect(Vec2(-2, -2), Vec2(-1, -1), '!')

# MUST BE USED, the unregister function is used twice before registering anything.
# since index 0 and 1 are unregistered, 2 objects must be added here.
# if index 0, 1, 2, and 3 are unregistered, then this needs to be done 4 times.
drawMan.registerRect(rr)
drawMan.registerRect(rr)

class Bullet:
    def __init__(self, index):
        self.pos = Vec2(7, 6)
        self.vel = Vec2(1, 0.5)
        self.size = Vec2(3, 2)
        self.index = index

        self.render = RenderRect(Vec2(0, 0), Vec2(0, 0), '*')
        self.collider = ColliderRect(Vec2(0, 0), Vec2(0, 0))

    def update(self, drawMan):
        # bullet movement
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        if (self.pos.x >= 106):
            self.vel.x = -1

        elif (self.pos.x <= 0):
            self.vel.x = 1

        if (self.pos.y >= 25):
            self.vel.y = -0.5

        elif (self.pos.y <= 0):
            self.vel.y = 0.5

        # dynamic object unregister and register
        self.render = RenderRect(self.pos, Vec2(self.pos.x + 3, self.pos.y + 2), '*')
        self.render.setOutlineChar('/')

        self.collider = ColliderRect(self.pos, Vec2(self.pos.x + 3, self.pos.y + 2))

        drawMan.unregisterRect(self.index)
        drawMan.registerRectId(self.render, self.index)

# construct a bullet
b0 = Bullet(1)

# construct the player
pPos = Vec2(0, 0)
pSize = Vec2(4, 3)
pRect = RenderRect(Vec2(0, 0), Vec2(0, 0), '#')
pCol = ColliderRect(Vec2(0, 0), Vec2(0, 0))

running = True

while running:
    # movement
    if (isKeyPressed('d')):
        pPos.x += 1
    if (isKeyPressed('a')):
        pPos.x -= 1
    if (isKeyPressed('s')):
        pPos.y += 0.5
    if (isKeyPressed('w')):
        pPos.y -= 0.5

    if (isKeyPressed('k')):
        running = False

    # unregister and register the player as it is dynamic
    pRect = RenderRect(pPos, Vec2(pPos.x + pSize.x, pPos.y + pSize.y), '#')
    pRect.setOutlineChar('=')

    pCol = ColliderRect(pPos, Vec2(pPos.x + pSize.x, pPos.y + pSize.y))

    drawMan.unregisterRect(0)
    drawMan.registerRectId(pRect, 0)

    b0.update(drawMan)

    if (pCol.isCollidingWith(b0.collider)):
        running = False

    game.update()
    sleeps(0.03)
