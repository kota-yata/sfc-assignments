import pyxel

class Pad:
  width = 40
  height = 30
  def __init__(self):
    self.x = 0
    self.y = 0
  def update(self):
    self.x = pyxel.mouse_x
    self.y = 190
  def draw(self):
    pyxel.rect(self.x, self.y, self.width, self.height, 0)
