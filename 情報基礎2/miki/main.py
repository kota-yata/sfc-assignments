import pyxel
from enum import Enum, auto
import random
import math

DISPLAY_WIDTH = 160
DISPLAY_HEIGHT = 120

BALL_RADIUS = 5

RACKET_LENGTH = 30
RACKET_DURATION = 3

class STATE (Enum):
  ON = auto()
  OVER = auto()

class Obstacle:
  def __init__(self, x, y, size):
    self.x = x
    self.y = y
    self.size = size
  def udpate(self):
    pass
  def draw(self):
    pyxel.rect(self.x, self.y, self.size, self.size, 9)

class Racket:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.length = RACKET_LENGTH
    self.duration = RACKET_DURATION

  def update(self):
    if (pyxel.btnp(pyxel.KEY_LEFT, 1, 1) and self.x > 0):
      self.x -= self.duration
    if (pyxel.btnp(pyxel.KEY_RIGHT, 1, 1) and self.x + self.length < DISPLAY_WIDTH):
      self.x += self.duration

  def draw(self):
    pyxel.rect(self.x, self.y, self.length, 2, 9)

class Ball:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.radius = BALL_RADIUS
    self.vx = 2
    self.vy = 2
    self.direction_x = -1
    self.direction_y = -1
    self.obstacle_is_touched = False
  
  def speed_up(self):
    self.vx = math.copysign(abs(self.vx) + 0.2, self.vx)
    self.vy = math.copysign(abs(self.vy) + 0.2, self.vy)

  def update_position(self):
    self.x += self.direction_x * self.vx
    self.y += self.direction_y * self.vy

  def update(self, racket, obstacle_x, obstacle_y, obstacle_size):
    if (self.y > (DISPLAY_HEIGHT - self.radius)):
      return STATE.OVER
    if ((self.y + self.radius > racket.y) and (self.x + self.radius > racket.x) and (self.x + self.radius < racket.x + RACKET_LENGTH)):
      self.direction_y = -1
      self.vy = 2
    if ((self.x > (DISPLAY_WIDTH - self.radius)) or (self.x < self.radius)):
      self.direction_x = -self.direction_x
    if (self.y < self.radius):
      self.direction_y = -self.direction_y
    # if the ball touches the bottom or the top of the obstacle, flip the y direction
    if ((self.y + self.radius > obstacle_y) and (self.y - self.radius < obstacle_y + obstacle_size) and (self.x + self.radius > obstacle_x) and (self.x - self.radius < obstacle_x + obstacle_size)):
      self.obstacle_is_touched = True
    self.update_position()
    return STATE.ON

  def draw(self):
    pyxel.circ(self.x, self.y, self.radius, 9)

class App:
  def __init__(self, width, height):
    pyxel.init(width, height, title="squash")
    self.balls = [Ball(50, 50)]
    self.racket = Racket(60, 100)
    self.obstacle = Obstacle(80, 30, 10)
    self.state = STATE.ON
    self.score = 0
    pyxel.run(self.update, self.draw)

  def update_on(self):
    ballStates = []
    for i in range(len(self.balls)):
      state = self.balls[i].update(self.racket, self.obstacle.x, self.obstacle.y, self.obstacle.size)
      ballStates.append(state)
    if STATE.OVER in ballStates:
      self.state = STATE.OVER

  def update_over(self):
    if pyxel.btnp(pyxel.KEY_SPACE):
      self.balls = [Ball(50, 50)]
      self.racket = Racket(60, 100)
      self.obstacle = Obstacle(80, 30, 10)
      self.state = STATE.ON
      self.score = 0

  def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    if self.state == STATE.ON:
      self.update_on()
    elif self.state == STATE.OVER:
      self.update_over()
    self.racket.update()
    for i in range(len(self.balls)):
      if self.balls[i].obstacle_is_touched:
        self.obstacle = Obstacle(random.randint(30, 140), random.randint(30, 80), random.randint(5, 15))
        self.balls[i].obstacle_is_touched = False
        self.balls[i].speed_up()
        self.score += 1
        if self.score % 5 == 0:
          self.balls.append(Ball(50, 50))
    self.obstacle.udpate()

  def draw(self):
    pyxel.cls(2)
    if self.state == STATE.ON:
      for i in range(len(self.balls)):
        self.balls[i].draw()
      self.racket.draw()
      self.obstacle.draw()
      pyxel.text(10, 10, "SCORE: " + str(self.score), 9)
    if self.state == STATE.OVER:
      pyxel.text(60, 50, "GAME OVER...", 9)
      pyxel.text(30, 60, "PRESS SPACE TO TRY AGAIN", 9)

App(DISPLAY_WIDTH, DISPLAY_HEIGHT)
