import pyxel
import shooter
import target

class Game:
    def __init__(self):
        # ゲームの初期化処理
        self.shooter = shooter.Shooter()  # シューターのオブジェクトを作成
        self.targets = [target.Target() for _ in range(10)]  # 10個のターゲットオブジェクトを作成
        self.start_time = pyxel.frame_count  # ゲーム開始時のフレーム数
        self.elapsed_time = 0  # 経過時間
        self.game_over = False  # ゲームオーバーフラグの初期化

    def update(self):
        if self.game_over:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.__init__()  # スペースキーが押されたらゲームを再初期化
        self.shooter.update()
        for target in self.targets:
            target.update()
            for bullet in self.shooter.bullets:
                # 当たり判定のチェック
                if bullet.active and target.alive and self.check_collision(bullet, target):
                    bullet.active = False
                    target.alive = False
        self.elapsed_time = (pyxel.frame_count - self.start_time) / 30  # 最初のフレームと今のフレームの差から経過時間を計算する
        if all(not target.alive for target in self.targets):
            self.game_over = True  # 全てのターゲットが破壊されたらゲームオーバー

    def check_collision(self, bullet, target):
        # 弾とターゲットの当たり判定
        return (bullet.x < target.x + target.width and
                bullet.x + 2 > target.x and
                bullet.y < target.y + target.height and
                bullet.y + 2 > target.y)

    def draw(self):
        pyxel.cls(0)  # 画面をクリア
        if self.game_over:
            # ゲームオーバー時のテキスト表示
            pyxel.text(60, 90, f"Time: {self.elapsed_time:.2f}sec", 7)
            pyxel.text(60, 100, "PRESS SPACE TO RESTART", 7)
        else:
            # ゲームプレイ中の描画処理
            pyxel.text(10, 10, f"{self.elapsed_time:.2f}", 7)
            self.shooter.draw()  # 射手の描画
            for target in self.targets:
                target.draw()  # 各ターゲットの描画

    def run(self):
        # ゲームループの開始
        pyxel.run(self.update, self.draw)

pyxel.init(200, 200)  # Pyxelの初期化、ウィンドウサイズを200x200に設定
game = Game()  # ゲームオブジェクトの作成
game.run()  # ゲームの実行
