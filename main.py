import pyxel

class App:
    def __init__(self):
        pyxel.init(224, 248, "Pac-Man", 30, pyxel.KEY_ESCAPE, 10)
        pyxel.load("theme.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 0, 0, 0, 0, 224, 248)

App()