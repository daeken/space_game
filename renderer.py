import pygame, random

import input, spaceship, dispatch, util

class Renderer:
    def __init__(self, size=(800, 600)):
        self.screen = pygame.display.set_mode(size)
        self.size = self.screen.get_size()
        self.bg = pygame.image.load('background1.bmp')
        self.bg = self.bg.convert(32, pygame.SRCALPHA)
        self.bgsize = self.bg.get_size()
        util.trans_to_clear(self.bg, self.bgsize)

        self.scroll = -self.bgsize[1] + self.size[1]

        self.LoadImages()

        self.allsprites = pygame.sprite.RenderPlain(())

        self.spaceships = {}
        self.Load(self.spaceships, 'first', 'first.bmp')
        self.Load(self.spaceships, 'second', 'second.bmp')
        self.Load(self.spaceships, 'third', 'third.bmp')

        self.Load(self.spaceships, 'enemy_1', 'enemy_1.bmp')
        self.Load(self.spaceships, 'enemy_2', 'enemy_2.bmp')

        self.dispatch = dispatch.Dispatcher(size, self.allsprites, self)
        self.spaceship = spaceship.Spaceship(self.dispatch, self.size, (100, 100), self.spaceships['second'])

        self.allsprites.add(self.spaceship)
        self.input = input.Input(self.spaceship)

        clock = pygame.time.Clock()

        while self.Tick():
            clock.tick(60)
            self.allsprites.update()
            self.Draw()

    def LoadImages(self):
        self.lasers = {}
        self.Load(self.lasers, 'blue', 'lasers/blue.bmp')
        self.Load(self.lasers, 'red', 'lasers/red.bmp')
        self.Load(self.lasers, 'big_gun', 'lasers/big gun.bmp')

    def Load(self, array, name, file):
        image = pygame.image.load(file)
        image = image.convert(32, pygame.SRCALPHA)
        util.trans(image, image.get_size())
        array[name] = image

    def Draw(self):
        self.screen.blit(self.bg, (0, self.scroll))
        if self.scroll > -self.size[1]:
            self.screen.blit(self.bg, (0, self.scroll + self.size[1]))

        if self.scroll >= 0:
            self.scroll = -self.bgsize[1] + self.size[1]

        self.scroll += 3
        
        self.allsprites.draw(self.screen)

        for fired in self.dispatch.fired:
            self.screen.blit(self.lasers[fired[2]], fired[0])
        
        pygame.display.flip()
        
    def Tick(self):
        if len(self.allsprites.sprites()) < 15:
            r = random.randrange(0, 25)
            if r == 1:
                self.dispatch.Enemy(self.size, (random.randrange(0, self.size[0]), 0), 'enemy_1')
            elif r == 2:
                self.dispatch.Enemy(self.size, (random.randrange(0, self.size[0]), 0), 'enemy_2')

        while True:
            event = pygame.event.poll()
            if event:
                if not self.input.Handler(event):
                    return False
            else:
                break
        return True
