import pyxel

class Ball:
    def __init__(self):
        # ボールの初期位置と速度を設定
        self.x = 0
        self.y = 0
        self.vx, self.vy = self.rand_angle()

    def rand_angle(self):
        # ボールの移動角度をランダムに生成し、その角度に基づく速度ベクトルを返す
        angle = pyxel.rndi(30, 150)
        vx = pyxel.cos(angle)
        vy = pyxel.sin(angle)
        return vx, vy

    def rand_x(self):
        # ボールのx座標をランダムに生成
        return pyxel.rndi(1, 199)

    def update(self, padx):
        # ボールの状態を更新（壁やパドルに衝突した場合の処理を含む）
        global speed
        self.x += self.vx * speed
        self.y += self.vy * speed
        if self.y >= 200:
            self.x = self.rand_x()
            self.y = 0
            self.vx, self.vy = self.rand_angle()
        if self.x >= 200 or self.x < 0:
            self.vx = -self.vx
        if self.y >= 195 and (self.x >= padx.x - 20 and self.x <= padx.x + 20):
            self.x = self.rand_x()
            self.y = 0
            self.vx, self.vy = self.rand_angle()
            speed += 0.5
            return 1
        return 0

    def draw(self):
        # ボールを画面に描画
        pyxel.circ(self.x, self.y, 10, 6)

class Pad:
    def __init__(self):
        # パドルの初期位置を設定
        self.x = 100

    def update(self):
        # パドルの位置を更新（マウスの位置に追従）
        self.x = pyxel.mouse_x

    def draw(self):
        # パドルを画面に描画
        pyxel.rect(self.x - 20, 195, 40, 5, 14)

# Pyxelのウィンドウサイズを200x200ピクセルに設定
pyxel.init(200, 200)

# ゲームの状態を初期化
balls = [Ball()]
padx = Pad()
score = 0
speed = 3

def update():
    # ゲームのロジックを更新
    global padx, score, speed
    padx.update()
    for ball in balls:
        score += ball.update(padx)
    if score >= 10:
        balls.append(Ball())
        score = 0
        speed = 3

def draw():
    # ゲームの画面を描画
    pyxel.cls(7)
    for ball in balls:
        ball.draw()
    padx.draw()
    pyxel.text(10, 10, "score: " + str(score), 6)

# Pyxelのメインループを開始
pyxel.run(update, draw)
