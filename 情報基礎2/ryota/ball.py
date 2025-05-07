import pyxel

class Ball:
  size = 20
  def __init__(self, x, y, vx, vy):
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.is_reflect = False
    self.is_active = True
    self.is_scored = False
  def update(self, pad_x, pad_y, pad_width,  bucket_x, bucket_y, bucket_width):
    self.x += self.vx
    self.y += self.vy
    # ボールが画面外（左右）に出たらxの進行方向を逆にして反射させる
    if self.x < 0 or self.x > pyxel.width - self.size:
      self.vx *= -1
    # ボールが画面外（上）に出たらyの進行方向を逆にして反射させる
    if self.y < 0:
      self.vy *= -1
    # ボールが画面外（下）に出たらis_activeをFalseにする
    if self.y > pyxel.height:
      self.is_active = False
    # ボールがパッドに当たったらyの進行方向を逆にして反射させる
    if self.y + self.size > pad_y and pad_x - self.size <= self.x <= pad_x + pad_width:
      self.is_reflect = True
      self.vy *= -1
    # ボールがバケツに入ったらis_scoredをTrueにする
    # ボールのy座標と横幅がバケツのy座標と横幅の範囲内にあり、尚且つ一度パッドに当たっているとき
    if bucket_y < self.y < bucket_y + self.size and bucket_x - self.size < self.x < bucket_x + bucket_width and self.is_reflect:
      if self.vy < 0:
        return
      self.is_scored = True
  def draw(self):
    pyxel.blt(self.x, self.y, 2, 0, 0, self.size, self.size, 0)
