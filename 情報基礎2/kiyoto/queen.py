import pyxel

class Queen:
  position_y = 180 - 15
  width = 10
  height = 15
  def __init__(self, x):
    self.position_x = x 
  def update(self):
    if pyxel.btn(pyxel.KEY_LEFT):
      self.position_x -= 1 if self.position_x > 0 else 0
    elif pyxel.btn(pyxel.KEY_RIGHT):
      self.position_x += 1 if self.position_x < pyxel.width - self.width else 0
  def draw(self):
    pyxel.rect(self.position_x, self.position_y, self.width, self.height, 8)
