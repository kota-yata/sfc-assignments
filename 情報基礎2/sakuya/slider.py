import pyxel

class Slider:
  def __init__(self):
    self.position = 0
    self.speed = 6
    self.color = 13
    self.is_moving = True
  def update(self):
    if not self.is_moving:
      return
    self.position += self.speed
    if self.color != 13:
      self.color = 13
    if self.position > 50 or self.position < 0:
      self.speed *= -1
  def stop(self):
    self.is_moving = False
    difference = self.get_difference_from_the_center()
    if difference == 0:
      self.color = 8
    elif difference < 5:
      self.color = 9
    elif difference < 10:
      self.color = 15
    return difference
  def move(self):
    self.is_moving = True
  def get_difference_from_the_center(self):
    return abs(self.position - 25)
  def draw(self):
    pyxel.circ(10, 120 + self.position, 2, self.color)