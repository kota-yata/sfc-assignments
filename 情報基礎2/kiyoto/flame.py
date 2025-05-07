import pyxel

class Flame:
  stage_height = 180
  def __init__(self, x, is_debuffing = False, is_buffing = False):
    self.position_x = x
    self.position_y = 0
    self.is_alive = True
    self.is_debuffing = is_debuffing
    self.is_buffing = is_buffing
    self.flame_size = 5
    if self.is_debuffing:
      self.color = 8
    elif self.is_buffing:
      self.color = 11
    else:
      self.color = 9
  def update(self):
    self.position_y += 1
    if self.position_y > self.stage_height:
      self.is_alive = False
  def draw(self):
    if self.is_alive:
      pyxel.rect(self.position_x, self.position_y, self.flame_size, self.flame_size, self.color)
