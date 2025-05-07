import pyxel
import random
import ball
import pad
import bucket

class Game:
  def __init__(self):
    # リスタート時と同じ処理をする
    self.restart()
    pyxel.init(200, 200)
    pyxel.mouse(True)
    # イラストデータを読み込む
    pyxel.load("img.pyxres")
    pyxel.run(self.update, self.draw)
  # ボール、パッド、バケツ、HP、スコア、ゲームオーバーかどうかを初期化する
  def restart(self):
    self.ball = ball.Ball(0, 0, 5, 5)
    self.pad = pad.Pad()
    self.bucket = bucket.Bucket(random.randint(50, 150), random.randint(30, 130))
    self.hp = 5
    self.score = 0
    self.is_over = False
  def update(self):
    # hpが0以下になったらゲームオーバー
    if self.hp <= 0:
      self.is_over = True
      # スペースキーを押したらリスタート
      if pyxel.btnp(pyxel.KEY_SPACE):
        self.restart()
    self.pad.update()
    self.ball.update(self.pad.x, self.pad.y, self.pad.width, self.bucket.x, self.bucket.y, self.bucket.width)
    self.bucket.update()
    # ボールが画面外（下）に出たらHPを減らす
    if not self.ball.is_active:
      self.hp -= 1
      self.ball = ball.Ball(random.randint(50, 150), 0, random.randint(-5, 5), 4)
    # ボールがバケツに入ったらスコアを増やす
    if self.ball.is_scored:
      self.score += 1
      self.ball = ball.Ball(random.randint(50, 150), 0, random.randint(-5, 5), 4)
      self.bucket = bucket.Bucket(random.randint(50, 150), random.randint(30, 130))
  def draw(self):
    pyxel.cls(4)
    # ゲームオーバーならゲームオーバー画面を表示する
    if self.hp <= 0:
      pyxel.text(80, 80, "GAME OVER", 0)
      pyxel.text(80, 90, "Press SPACE to restart", 0)
      return
    pyxel.text(5, 5, "HP: " + str(self.hp), 3)
    pyxel.text(5, 10, "Score: " + str(self.score), 3)
    self.pad.draw()
    self.ball.draw()
    self.bucket.draw()

Game()
