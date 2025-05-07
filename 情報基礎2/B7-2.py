import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x_to = 0
y_to = 0

def update():
  global x_to, y_to
  if pyxel.btn(pyxel.KEY_SPACE):
    x_to = pyxel.mouse_x
    y_to = pyxel.mouse_y

def draw():
  pyxel.cls(7)
  pyxel.line(0, 0, x_to, y_to, 0)

pyxel.run(update, draw)
