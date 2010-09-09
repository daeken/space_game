import pygame

MOVE_DOWN = 1
MOVE_UP = 2
MOVE_LEFT = 4
MOVE_RIGHT = 8

class Input:
    def __init__(self, spaceship):
        self.spaceship = spaceship
        pygame.key.set_repeat(1, 500)

        pygame.mouse.set_visible(False)
    def Handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.spaceship.Move(MOVE_UP)
            elif event.key == pygame.K_DOWN:
                self.spaceship.Move(MOVE_DOWN)
            elif event.key == pygame.K_LEFT:
                self.spaceship.Move(MOVE_LEFT)
            elif event.key == pygame.K_RIGHT:
                self.spaceship.Move(MOVE_RIGHT)
            elif event.unicode == ' ':
                self.spaceship.Fire()
            elif event.unicode == 's':
                self.spaceship.Fire()
            elif event.key == pygame.K_ESCAPE:
                return False
        elif event.type == pygame.MOUSEMOTION:
            self.spaceship.pos = list(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.spaceship.Fire()
        elif event.type == pygame.QUIT:
            return False
        return True
