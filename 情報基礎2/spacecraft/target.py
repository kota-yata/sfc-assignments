import pyxel
import random
import math

class Target:
    def __init__(self):
        # ターゲットの位置とサイズ
        self.center_x = random.randint(20, pyxel.width - 20)
        self.center_y = random.randint(20, 150)
        self.radius = random.randint(10, 20)
        self.angle = 0
        self.speed = random.random() * 0.1
        self.width = 5
        self.height = 5
        self.alive = True

    def update(self):
        self.angle += self.speed
        self.x = self.center_x + math.cos(self.angle) * self.radius
        self.y = self.center_y + math.sin(self.angle) * self.radius

    def draw(self):
        # ターゲットを描画
        if self.alive:
            pyxel.rect(self.x, self.y, self.width, self.height, 8)
