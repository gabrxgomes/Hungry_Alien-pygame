import pygame


class Obj:

    def __init__(self, image, x, y):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        self.frame = 1
        self.tick = 0

    def draw(self, window):
        self.group.draw(window)

    def anim(self, image, tick, frames):
        self.tick += 1
        if self.tick == tick:
            self.tick = 0
            self.frame += 1
            #separando entre animações de fps e de frames
        if self.frame == frames:
            self.frame = 1

        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")


        # aqui em cima tem q ser o nome do sprite sem a numeração, se não ele soma os valores sprite1 + valor 1 = sprite11


class Alien(Obj):

    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        self.life = 3
        self.pts = 0




    def move_alien(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 30
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 34

    def colision(self, group, name):
        name = name
        colision = pygame.sprite.spritecollide(self.sprite, group, True) #TRUE AQUI PARA DESTRUIR O OBJETO COLIDIDO E FALSE PARA NAO DESTRUIR

        if name == "coracao" and colision:
            self.pts += 1  #soma 1

        elif name == "espinho" and colision:
            self.life -= 1  #tira 1


class Text:

    def __init__(self, size, text):

        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, True, (255,255,255)) #o true é pergutando se queremos uma imagem bem lisa

    def draw(self, window, x, y):
        window.blit(self.render, (x,y))

    def update_text(self, update):
        self.render = self.font.render(update, False, (255, 255, 255))


