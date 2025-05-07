import pyxel
import bullet

class Shooter:
    def __init__(self):
        # シューターの初期位置とサイズ
        self.x = pyxel.width / 2
        self.y = pyxel.height - 5
        self.width = 20
        self.height = 5
        self.bullets = []

    def update(self):
        # シューターを左右に動かす
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2

        # 画面端の処理
        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.width)

        if pyxel.btnp(pyxel.KEY_SPACE):
            self.bullets.append(bullet.Bullet(self.x + self.width / 2 - 1, self.y, 2))

        for b in self.bullets:
            b.update()

        self.bullets = [bullet for bullet in self.bullets if bullet.active]

    def draw(self):
        # シューターを描画
        pyxel.rect(self.x, self.y, self.width, self.height, 11)
        for bullet in self.bullets:
            bullet.draw()
