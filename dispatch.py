import spaceship, enemy, projectile

class Dispatcher:
    def __init__(self, size, sprites, ren):
        self.ren = ren
        self.sprites = sprites
        self.size = size
        self.spaceships = []
        self.fired = []
    def Enemy(self, wsize, pos, image):
        self.sprites.add(enemy.Enemy(wsize, self, pos, self.ren.spaceships[image]))
    def Fire(self, image, pos, dir, enemy=False):
        self.sprites.add(projectile.Projectile(self.sprites, self.ren.lasers[image], self.size, pos, dir, enemy))
    def Tick(self):
        fired = []
        for x in self.fired:
            if x[0][0] >= 0 and x[0][0] < self.size[0] and x[0][1] >= 0 and x[0][1] < self.size[1]:
                x[0][0] += x[1][0]
                x[0][1] += x[1][1]
                fired.append(x)
        self.fired = fired
