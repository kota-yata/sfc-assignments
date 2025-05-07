import pyxel

pyxel.init(200, 200)

ballxs = [pyxel.rndi(0, 199), pyxel.rndi(0, 199), pyxel.rndi(0, 199),]
ballys = [0, 0, 0]
angles = [pyxel.rndi(30, 150), pyxel.rndi(30, 150), pyxel.rndi(30, 150)]

vxs = []
vys = []

for i in range(0, len(angles)):
    vxs.append(pyxel.cos(angles[i]))
    vys.append(pyxel.sin(angles[i]))

padx = 100
speed = 2
score = 0

def update():
    global ballxs, ballys, vxs, vys, speed, score, padx
    padx = pyxel.mouse_x
    for i in range(0, len(angles)):
        ballxs[i] += vxs[i] * speed
        ballys[i] += vys[i] * speed
        if ballys[i] >= 200:
            ballxs[i] = pyxel.rndi(0, 199)
            ballys[i] = 0
            vxs[i] = pyxel.cos(pyxel.rndi(30, 150))
            vys[i] = pyxel.sin(pyxel.rndi(30, 150))
        if ballxs[i] >= 200 or ballxs[i] < 0:
            vxs[i] = -vxs[i]
        if ballys[i] >= 195 and (ballxs[i] >= padx - 20 and ballxs[i] <= padx):
            ballxs[i] = pyxel.rndi(0, 199)
            ballys[i] = 0
            vxs[i] = pyxel.cos(pyxel.rndi(30, 150))
            vys[i] = pyxel.sin(pyxel.rndi(30, 150))
            score += 1

def draw():
    pyxel.cls(7)
    for i in range(0, len(angles)):
        pyxel.circ(ballxs[i], ballys[i], 10, 6)
    pyxel.rect(padx - 20, 195, 40, 5, 14)
    pyxel.text(10, 10, "score: " + str(score), 6)

pyxel.run(update, draw)
