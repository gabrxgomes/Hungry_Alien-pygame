import pygame

from menu import Menu, GameOver
from game import Game


class Main:

    def __init__(self):

        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load("sounds/videoplayback.ogg")
        pygame.mixer.music.play(-1) #o menos 1 define q vai tocar a musica o tempo
        pygame.mixer.music.set_volume(0.2)



        self.window = pygame.display.set_mode([300, 500])
        pygame.display.set_caption("HungryAlien")

        self.menu = Menu("assets/tela de start.png")
        self.game = Game()
        self.gameover = GameOver("assets/tela de gameover.png")

        self.loop = True
        self.fps = pygame.time.Clock()

    def draw(self):

        if not self.menu.change_scene:
            self.menu.draw(self.window)
        elif not self.game.change_scene:

            self.game.draw(self.window)
            self.game.update()

        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)
        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.alien.life = 3
            self.game.alien.pts = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

            if not self.menu.change_scene:

                self.menu.event(event)
            elif not self.game.change_scene:
                self.game.alien.move_alien(event)
            else:
                self.gameover.event(event)

    def update(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pygame.display.update()


Main().update()
