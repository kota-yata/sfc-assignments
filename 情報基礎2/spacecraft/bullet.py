import pyxel

class Bullet:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.active = True

    def update(self):
        if self.active:
            self.y -= self.speed
            if self.y < 0:
                self.active = False

    def draw(self):
        if self.active:
            pyxel.rect(self.x, self.y, 2, 2, 7)