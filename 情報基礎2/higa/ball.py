import pyxel

class Ball:
  def __init__(self):
    self.x = 160
    self.y = 200
    self.speed = 4
    self.is_kicked = False
    self.is_done = False
    self.is_blocked = False
  def update(self):
    if not self.is_kicked:
      return
    self.y -= self.speed
    if (self.is_blocked and self.y < 25) or (not self.is_blocked and self.y < 0):
      self.is_kicked = False
      self.is_done = True
      self.y = 200
  def kick(self, x, is_blocked):
    self.is_blocked = is_blocked
    if self.is_kicked:
      return
    self.is_kicked = True
    self.x = x
  def draw(self):
    pyxel.circ(self.x, self.y, 4, 7)
