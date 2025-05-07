import pyxel

class Ball:
    def __init__(self):
        self.restart()
    
    def restart(self):
        self.x = pyxel.rndi(0, 199)    #0から画面の横幅-1の間
        self.y = 0
        angle = pyxel.rndi(30, 150)    #30度から150度の間
        self.vx = pyxel.cos(angle)
        self.vy = pyxel.sin(angle)

    def rand_angle(self):
        angle = pyxel.rndi(30, 150)
        vx = pyxel.cos(angle)
        vy = pyxel.sin(angle)
        return vx, vy

    def rand_x(self):
        return pyxel.rndi(1, 199)
    
    def move(self):
        self.x += self.vx * speed
        self.y += self.vy * speed

    def update(self, padx):
        global speed
        self.move()
        if self.y >= 200:
            self.x = self.rand_x()
            self.y = 0
            self.vx, self.vy = self.rand_angle()
        if self.x >= 200 or self.x < 0:
            self.vx = -self.vx
        if padx.touch(self):
            self.restart()
            speed += 0.5
            return 1
        return 0

    def draw(self):
        pyxel.circ(self.x, self.y, 10, 6)

class Pad:
    def __init__(self):
        self.x = 100
    def update(self):
        self.x = pyxel.mouse_x
    def draw(self):
        pyxel.rect(self.x - 20, 195, 40, 5, 14)
    def touch(self, ball):
        if ball.y >= 195 and (ball.x >= self.x - 20 and ball.x <= self.x + 20):
            return True
        return False

pyxel.init(200, 200)

balls = [Ball()]

padx = Pad()
score = 0
speed = 3

def update():
    global padx, score, speed
    padx.update()
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
    padx.draw()
    pyxel.text(10, 10, "score: " + str(score), 6)

pyxel.run(update, draw)
