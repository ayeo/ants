import pygame

from core.Ant import Ant

class AntSprite(pygame.sprite.Sprite):
    def __init__(self, ant: Ant, pos, tail_size, ant_color):
        pygame.sprite.Sprite.__init__(self)
        self.id = ant.id
        self.ant = ant
        self.image = pygame.Surface((tail_size, tail_size))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.ant_color = ant_color

    def update(self, *args):
        if (self.ant.carrying):
            self.image.fill((255, 0, 0))
        else:
            self.image.fill(self.ant_color)

    def change_position(self, pos):
        self.rect.center = pos
