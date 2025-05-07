import pyxel
import ball
import random

class PKGame:
    def __init__(self):
        pyxel.init(320, 240)  # ウィンドウサイズを320x240に変更
        pyxel.mouse(True)
        self.score_kicker = []
        self.score_keeper = []
        self.round = 1
        self.kicker_position = 0
        self.keeper_position = 0
        self.ball = ball.Ball()
        self.goalkeeper_x = 150
        self.goalkeeper_y = 20
        self.is_finished = False
        pyxel.run(self.update, self.draw)

    def update(self):
        if self.is_finished:
            if pyxel.btnp(pyxel.KEY_R):
                self.score_kicker = []
                self.score_keeper = []
                self.round = 1
                self.kicker_position = 0
                self.keeper_position = 0
                self.ball = ball.Ball()
                self.goalkeeper_x = 150
                self.goalkeeper_y = 20
                self.is_finished = False
            return
        if pyxel.btnp(pyxel.KEY_1):
            self.kicker_position = 1
            self.updateKeeper()
            self.ball.kick(140, self.kicker_position == self.keeper_position)
        elif pyxel.btnp(pyxel.KEY_2):
            self.kicker_position = 2
            self.updateKeeper()
            self.ball.kick(160, self.kicker_position == self.keeper_position)
        elif pyxel.btnp(pyxel.KEY_3):
            self.kicker_position = 3
            self.updateKeeper()
            self.ball.kick(180, self.kicker_position == self.keeper_position)
        self.ball.update()
        if self.ball.is_done:
            success = self.kicker_position != self.keeper_position
            self.score_kicker.append("S" if success else "F")
            self.score_keeper.append("F" if success else "S")
            self.kicker_position = 0
            self.round += 1
            self.ball.is_done = False
            if self.round > 5:
                self.is_finished = True
    def updateKeeper(self):
        randint = random.randint(1, 10)
        candidates = [130, 150, 170]
        if randint < 5:
            self.keeper_position = self.kicker_position
            self.goalkeeper_x = candidates[self.kicker_position - 1]
        else:
            diff = (self.kicker_position + 1) % 3
            self.keeper_position = 3 if diff == 0 else diff
            self.goalkeeper_x = candidates[(self.kicker_position + 1) % 3]

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(120, 0, 80, 10, 8)
        pyxel.rect(self.goalkeeper_x, self.goalkeeper_y, 20, 10, 9)
        self.ball.draw()
        pyxel.text(10, 220, "Kicker", 7)
        pyxel.text(10, 230, "Keeper", 7)
        for i in range(2):
            for j in range(5):
                pyxel.text(50 + j * 20, 220 - i * 10, self.score_kicker[i * 5 + j] if len(self.score_kicker) > i * 5 + j else "", 7)
                pyxel.text(50 + j * 20, 230 - i * 10, self.score_keeper[i * 5 + j] if len(self.score_keeper) > i * 5 + j else "", 7)

        # ゲーム終了
        if self.is_finished:
            kicker_wins = self.score_kicker.count("S") >= 3
            result_text = "Kicker Wins!" if kicker_wins else "Keeper Wins!"
            text_x = (pyxel.width - len(result_text) * pyxel.FONT_WIDTH) // 2
            text_y = (pyxel.height - pyxel.FONT_HEIGHT) // 2
            pyxel.text(text_x, text_y, result_text, 12)

if __name__ == "__main__":
    PKGame()
