import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

x_from = 0
y_from = 0

x_to = 0
y_to = 0

def update():
  global x_from, y_from, x_to, y_to
  if pyxel.btnp(pyxel.KEY_SPACE):
    x_from = pyxel.mouse_x
    y_from = pyxel.mouse_y
  elif pyxel.btn(pyxel.KEY_SPACE):
    x_to = pyxel.mouse_x
    y_to = pyxel.mouse_y

def draw():
  pyxel.cls(7)
  pyxel.line(x_from, y_from, x_to, y_to, 0)

pyxel.run(update, draw)
