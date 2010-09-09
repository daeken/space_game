import pygame, sys

class Ball(pygame.sprite.Sprite):
    def __init__(self, dir=None):
        self.rad, self.dir, self.pos, self.area = 2, [2,3], [200, 200], (400, 400)
        if dir:
            self.dir = dir
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.rad * 2, self.rad * 2))
        self.image.fill((0, 0, 0))
        self.rect = pygame.Rect(self.pos + [self.rad * 2, self.rad * 2])

    def update(self):
        self.pos[0] += self.dir[0]
        self.pos[1] += self.dir[1]

        if self.pos[0] - self.rad <= 0:
            self.dir[0] = -self.dir[0]
        elif self.pos[0] + self.rad >= self.area[0]:
            self.dir[0] = -self.dir[0]

        if self.pos[1] - self.rad <= 0:
            self.dir[1] = -self.dir[1]
        elif self.pos[1] + self.rad >= self.area[1]:
            self.dir[1] = -self.dir[1]

        self.rect = pygame.Rect(self.pos + [self.rad * 2, self.rad * 2])

class Example:
    screen, bg = None, None
    dir = [1, 1]
    pos = [200, 200]
    size = (400, 400)
    ball = None
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.Main()
        
    def Main(self):
        self.bg = pygame.Surface(self.screen.get_size()).convert()
        self.bg.fill((255, 255, 255))
        clock = pygame.time.Clock()
        self.ball = Ball()
        self.ball2 = Ball([1, 5])
        self.allsprites = pygame.sprite.RenderPlain((self.ball, self.ball2))

        while 1:
            clock.tick(60)

            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break
            
            self.allsprites.update()
            self.Draw()

    def Draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.allsprites.draw(self.screen)
        pygame.display.flip()

def main():
    ex = Example()

if __name__=='__main__':
    sys.exit(main())
