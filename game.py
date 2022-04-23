from obj import Obj, Alien, Text
import random


class Game:

    def __init__(self):

        self.bg = Obj("assets/fundo.png", 0, 0)

        self.espinho = Obj("assets/espinho1.png", random.randrange(0, 300), -50)
        self.coracao = Obj("assets/coracao1.png", random.randrange(0, 300), -50)

        self.alien = Alien("assets/alien1.png", 120, 420)  # está centralizado


        self.change_scene = False

        self.score = Text(120, "0")
        self.lifes = Text(60, "3")


    def draw(self, window):
        self.bg.draw(window)
        self.espinho.draw(window)
        self.coracao.draw(window)
        self.alien.draw(window)
        self.score.draw(window, 130, 25)
        self.lifes.draw(window, 25, 25)

    def update(self):
        self.espinho.anim("espinho", 8, 3)
        self.coracao.anim("coracao", 8, 5)  # sempre um frame a mais -----> frame/numero de sprites + 1
        self.alien.anim("alien", 5, 3)
        self.move_espinho()
        self.move_coracao()
        self.alien.colision(self.coracao.group, "coracao")
        self.alien.colision(self.espinho.group, "espinho")
        self.gameover()
        self.score.update_text(str(self.alien.pts))
        self.lifes.update_text(str(self.alien.life))

    def move_espinho(self):
        self.espinho.sprite.rect[1] += 10
        if self.espinho.sprite.rect[1] >= 540:
            self.espinho.sprite.kill()
            self.espinho = Obj("assets/espinho1.png", random.randrange(0, 300), -50)

    def move_coracao(self):
        self.coracao.sprite.rect[1] += 6

        if self.coracao.sprite.rect[1] >= 540:
            self.coracao.sprite.kill()
            self.coracao = Obj("assets/coracao1.png", random.randrange(0, 300), -50)


    def gameover(self):
        if self.alien.life <= 0:
            self.change_scene = True


