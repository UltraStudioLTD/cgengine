from cgengine import *

# construct the game and managers
drawMan = DrawManager(110, 28, ".")
gameMan = GameManager(drawMan)
game = Game(gameMan)

rr = RenderRect(Vector(-2, -2), Vector(-1, -1), "!")

# MUST BE USED, the unregister function is used twice before registering anything.
# since index 0 and 1 are unregistered, 2 objects must be added here.
# if index 0, 1, 2, and 3 are unregistered, then this needs to be done 4 times.
drawMan.registerRect(rr)
drawMan.registerRect(rr)


class Bullet:
    def __init__(self, index):
        self.pos = Vector(7, 6)
        self.vel = Vector(1, 0.5)
        self.size = Vector(3, 2)
        self.index = index

        self.render = RenderRect(Vector(0, 0), Vector(0, 0), "*")
        self.collider = ColliderRect(Vector(0, 0), Vector(0, 0))

    def update(self, drawMan):
        # bullet movement
        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

        if self.pos.x >= 106:
            self.vel.x = -1

        elif self.pos.x <= 0:
            self.vel.x = 1

        if self.pos.y >= 25:
            self.vel.y = -0.5

        elif self.pos.y <= 0:
            self.vel.y = 0.5

        # dynamic object unregister and register
        self.render = RenderRect(self.pos, Vector(self.pos.x + 3, self.pos.y + 2), "*")
        self.render.setOutlineChar("/")

        self.collider = ColliderRect(self.pos, Vector(self.pos.x + 3, self.pos.y + 2))

        drawMan.unregisterRect(self.index)
        drawMan.registerRectId(self.render, self.index)


# construct a bullet
b0 = Bullet(1)

# construct the player
pPos = Vector(0, 0)
pSize = Vector(4, 3)
pRect = RenderRect(Vector(0, 0), Vector(0, 0), "#")
pCol = ColliderRect(Vector(0, 0), Vector(0, 0))

running = True

while running:
    # movement
    if isKeyPressed("d"):
        pPos.x += 1
    if isKeyPressed("a"):
        pPos.x -= 1
    if isKeyPressed("s"):
        pPos.y += 0.5
    if isKeyPressed("w"):
        pPos.y -= 0.5

    if isKeyPressed("k"):
        running = False

    # unregister and register the player as it is dynamic
    pRect = RenderRect(pPos, Vector(pPos.x + pSize.x, pPos.y + pSize.y), "#")
    pRect.setOutlineChar("=")

    pCol = ColliderRect(pPos, Vector(pPos.x + pSize.x, pPos.y + pSize.y))

    drawMan.unregisterRect(0)
    drawMan.registerRectId(pRect, 0)

    b0.update(drawMan)

    if pCol.isCollidingWith(b0.collider):
        running = False

    game.update()
    sleeps(0.03)
