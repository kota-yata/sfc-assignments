import pyxel

pyxel.init(200,200)

ballx = 0
bally = 0
vx = 0.866
vy = 0.5
padx = 100
speed = 3
score = 0

def rand():
    angle = pyxel.rndi(30, 150)
    vx = pyxel.cos(angle)
    vy = pyxel.sin(angle)
    return (vx, vy)

def update():
    global ballx, bally, vx, vy, padx, score
    ballx += vx * speed
    bally += vy * speed
    padx = pyxel.mouse_x
    if bally >= 200:
        ballx = 0
        bally = 0
        (vx, vy) = rand()
    if ballx >= 200 or ballx < 0:
        vx = -vx
    if bally >= 195 and (ballx >= padx - 20 and ballx <= padx):
        ballx = 0
        bally = 0
        (vx, vy) = rand()
        score += 1

def draw():
    global ballx, bally, vx, vy, padx
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx - 20, 195, 40, 5, 14)
    pyxel.text(10, 10, "score: " + str(score), 6)

pyxel.run(update, draw)
