import pyxel

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx, self.vy = self.rand_angle()

    def rand_angle(self):
        angle = pyxel.rndi(30, 150)
        vx = pyxel.cos(angle)
        vy = pyxel.sin(angle)
        return vx, vy

    def rand_x(self):
        return pyxel.rndi(1, 199)

    def update(self, padx):
        global speed
        self.x += self.vx * speed
        self.y += self.vy * speed
        if self.y >= 200:
            self.x = self.rand_x()
            self.y = 0
            self.vx, self.vy = self.rand_angle()
        if self.x >= 200 or self.x < 0:
            self.vx = -self.vx
        if self.y >= 195 and (self.x >= padx - 20 and self.x <= padx + 20):
            self.x = self.rand_x()
            self.y = 0
            self.vx, self.vy = self.rand_angle()
            speed += 0.5
            return 1
        return 0

    def draw(self):
        pyxel.circ(self.x, self.y, 10, 6)

pyxel.init(200, 200)

balls = [Ball()]

padx = 100
score = 0
speed = 3

def update():
    global padx, score, speed
    padx = pyxel.mouse_x
    for ball in balls:
        score += ball.update(padx)
    if score >= 10:
        balls.append(Ball())
        score = 0
        speed = 3

def draw():
    pyxel.cls(7)
    for ball in balls:
        ball.draw()
    pyxel.rect(padx - 20, 195, 40, 5, 14)
    pyxel.text(10, 10, "score: " + str(score), 6)

pyxel.run(update, draw)
