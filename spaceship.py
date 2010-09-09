import input, util, sound

import pygame, random

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, dispatch, wsize, pos, image):
        pygame.sprite.Sprite.__init__(self)

        self.type = 'player'

        self.dispatch = dispatch
        self.wsize = wsize
        self.life = 100
        self.pos = [float(pos[0]), float(pos[1])]

        self.move = 10

        self.image = image
        self.size = list(self.image.get_size())

    def Move(self, dir=0, loc=None):
        if dir & input.MOVE_UP:
            if self.pos[1] != self.size[1]:
                self.pos[1] -= self.move
        elif dir & input.MOVE_DOWN:
            if self.pos[1] != self.size[1]:
                self.pos[1] += self.move
        elif dir & input.MOVE_LEFT:
            if self.pos[0] != self.size[0]:
                self.pos[0] -= self.move
        elif dir & input.MOVE_RIGHT:
            if self.pos[0] != self.size[0]:
                self.pos[0] += self.move

        if loc:
            self.pos = loc

        pygame.mouse.set_pos(self.pos)
    def Fire(self):
        self.dispatch.Fire('blue', [self.pos[0] + (self.size[0] / 2), self.pos[1]], (0, -10), False)
    def update(self):
        self.rect = pygame.Rect(self.pos + self.size)

        collision = pygame.sprite.spritecollide(self, self.dispatch.sprites, False)
        for sprite in collision:
            if sprite == self:
                continue

            if sprite.type == 'enemy':
                self.dispatch.sprites.remove(sprite)
                self.Move(0, [random.randrange(0, self.wsize[0]), random.randrange(0, self.wsize[1])])
                self.update()
 
            elif sprite.type == 'projectile':
                if sprite.enemy:
                    self.dispatch.sprites.remove(sprite)
                    self.Move(0, [random.randrange(0, self.wsize[0]), random.randrange(0, self.wsize[1])])
                    self.update()


        for sprite in self.dispatch.sprites.sprites():
            if sprite.type == 'projectile' and not sprite.enemy:
                collision = pygame.sprite.spritecollide(sprite, self.dispatch.sprites, False)
                for spr in collision:
                    if (spr.type == 'enemy' or spr.type == 'player' or spr.enemy) and spr != sprite and spr != self:
                        self.dispatch.sprites.remove(sprite)
                        self.dispatch.sprites.remove(spr)
