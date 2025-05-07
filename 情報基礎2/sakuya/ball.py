import pyxel

class Ball:
  gravity = 0.98
  def __init__(self, x, y):
    self.is_moving = False
    self.is_done = False
    self.x = x
    self.y = y
    self.vx = 0
    self.vy = 0
  def update(self):
    if not self.is_moving:
      return
    self.x += self.vx
    self.y += self.vy
    self.vy += self.gravity
    if self.y > pyxel.height:
      self.is_moving = False
      self.is_done = True
  def start_moving(self, vx, vy):
    self.vx = vx
    self.vy = vy
    self.is_moving = True
    self.is_done = False
  def draw(self):
    if not self.is_moving:
      return
    pyxel.blt(self.x, self.y, 0, 0, 0, 100, 100, 0)
