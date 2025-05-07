import pyxel

pyxel.init(200,200)

a = 0
b = 1

def update():
  global a, b
  a += b
  if pyxel.btnp(pyxel.KEY_SPACE):
    b = -b

def draw():
  global a
  pyxel.cls(7)
  pyxel.circ(a, a, 10, 0)

pyxel.run(update, draw)
