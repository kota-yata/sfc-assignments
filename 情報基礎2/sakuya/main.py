import pyxel
import ball
import slider
import time
import random

class Game:
  vx = 7
  vy_success = -14
  vy_fail = -12
  def __init__(self):
    self.ball = ball.Ball(30, 140)
    self.slider = slider.Slider()
    self.score = 0
    self.result_reserved = 0
    self.is_sleeping = False
    pyxel.init(240, 180)
    pyxel.mouse(True)
    pyxel.load("img.pyxres")
    pyxel.run(self.update, self.draw)
  def update(self):
    if self.ball.is_done and not self.slider.is_moving:
      self.score += self.result_reserved
      self.result_reserved = 0
      self.is_sleeping = True
    if self.is_sleeping:
      time.sleep(2)
      self.is_sleeping = False
      self.slider.move()
      self.ball.is_done = False
    if pyxel.btnp(pyxel.KEY_SPACE) and not self.ball.is_moving:
      diff = self.slider.stop()
      self.ball = ball.Ball(10, 140)
      vy = self.vy_fail
      if diff == 0:
        self.result_reserved = 3
        vy = self.vy_success
      elif diff < 5:
        rand = random.randint(0, 1)
        self.result_reserved = 3 if rand == 0 else 2
        vy = self.vy_success
      elif diff < 10:
        rand = random.randint(0, 3)
        self.result_reserved = 2 if rand == 0 else 0
        vy = self.vy_success if rand == 0 else self.vy_fail
      self.ball.start_moving(self.vx, vy)
    self.ball.update()
    self.slider.update()
  def draw(self):
    pyxel.cls(4)
    if self.ball.is_done and self.result_reserved > 0:
      pyxel.text(110, 60, "Scored! +" + str(self.result_reserved), 0)
    elif self.ball.is_done:
      pyxel.text(110, 60, "Miss...", 0)
    pyxel.text(10, 10, "Score: " + str(self.score), 0)
    pyxel.blt(210, 110, 1, 0, 0, 100, 100, 0)
    pyxel.rect(30, 140, 20, 40, 0)
    pyxel.rect(10, 115, 1, 60, 7)
    self.ball.draw()
    self.slider.draw()

Game()
