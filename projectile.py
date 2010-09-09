import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, proj, image, wsize, pos, dir, enemy=False):
        pygame.sprite.Sprite.__init__(self)

        self.type = 'projectile'

        self.proj = proj
        self.image = image
        self.wsize = wsize
        self.pos = pos
        self.dir = dir

        self.enemy = enemy
        
        self.size = list(self.image.get_size())
        self.update()

    def update(self):
        self.rect = pygame.Rect(self.pos + self.size)

        if self.pos[0] >= 0 and self.pos[0] < self.wsize[0] and self.pos[1] >= 0 and self.pos[1] < self.wsize[1]:
            self.pos[0] += self.dir[0]
            self.pos[1] += self.dir[1]
        else:
            self.proj.remove(self)
