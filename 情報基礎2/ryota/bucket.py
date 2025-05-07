import pyxel

class Bucket:
  width = 20
  height = 20
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.is_active = True
  def update(self):
    pass
  def draw(self):
    # バケツの画像を描画する
    pyxel.blt(self.x, self.y, 1, 0, 0, self.width, self.height, 0)
