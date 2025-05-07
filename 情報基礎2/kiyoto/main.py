import pyxel
import flame
import queen
import random

class Game:
  def __init__(self):
    pyxel.init(200, 200)
    self.reset()
    pyxel.run(self.update, self.draw)

  def reset(self):
    self.flames = [flame.Flame(80)]
    self.queen = queen.Queen(80)
    self.frame_interval = 20
    self.reset_frame_count = 0
    self.score = 0
    self.hp = 3

  def update(self):
    if self.hp <= 0:
      if pyxel.btn(pyxel.KEY_SPACE):
        self.reset()
      return
    if pyxel.frame_count % self.frame_interval == 0:
      ri = random.randint(0, 5)
      position_x = random.randint(10, 190)
      self.flames.append(flame.Flame(position_x, is_debuffing = ri > 2, is_buffing = ri == 1))
    if pyxel.frame_count % 40 == 0:
      self.frame_interval -= 1 if self.frame_interval > 5 else 0
    for f in self.flames:
      if not f.is_alive:
        self.flames.remove(f)
      if f.position_y + f.flame_size > self.queen.position_y and f.position_x + f.flame_size > self.queen.position_x and f.position_x < self.queen.position_x + self.queen.width:
        if f.is_debuffing:
          self.hp -= 1
          self.frame_interval = 3
          self.reset_frame_count = pyxel.frame_count + 100
        elif f.is_buffing:
          self.score += 1
          self.frame_interval = 30
          self.reset_frame_count = pyxel.frame_count + 50
        else:
          self.hp -= 1
        self.flames.remove(f) if f in self.flames else None
        f.is_alive = False
      f.update()
    self.queen.update()

  def draw(self):
    pyxel.cls(0)
    if self.hp <= 0:
      pyxel.text(80, 80, "GAME OVER", 8)
      pyxel.text(80, 90, "SCORE: " + str(self.score), pyxel.frame_count % 16)
      pyxel.text(55, 100, "PRESS SPACE TO RESTART", 8)
      return
    for flame in self.flames:
      flame.draw()
    self.queen.draw()
    pyxel.rect(0 , 180, 200, 20, 9)
    pyxel.text(10, 10, "SCORE: " + str(self.score), 9)
    pyxel.text(10, 20, "HP: " + str(self.hp), 9)

Game()
