import spaceship

import pygame, random

class Enemy(spaceship.Spaceship):
    def __init__(self, wsize, dispatch, pos, image):
        self.wsize = wsize

        self.dir = 0
        
        spaceship.Spaceship.__init__(self, dispatch, wsize, pos, image)

        self.type = 'enemy'

        self.update()
        
    def Fire(self):
        self.dispatch.Fire('red', [self.pos[0] + (self.size[0] / 2), self.pos[1] + self.size[1]], (0, 10), True)

    def update(self):
        if random.randrange(0, 25) == 5:
            self.Fire()

        rand = random.randrange(0, 25)
        if rand == 0:
            self.dir = 1
        elif rand == 1:
            self.dir = 2

        self.pos[1] += 2

        if self.dir == 1:
            self.pos[0] -= 1
        elif self.dir == 2:
            self.pos[0] += 1

        if self.pos[0] < 0:
            self.pos[0] = 0
            self.dir = 0
        elif self.pos[0] > self.wsize[0]:
            self.pos[0] = self.wsize[0]
            self.dir = 0

        if self.pos[1] < 0:
            self.pos[1] = 0
            self.dir = 0
        elif self.pos[1] > self.wsize[1]:
            self.pos[1] = 0
            self.dir = 0
        
        self.rect = pygame.Rect(self.pos + self.size)
