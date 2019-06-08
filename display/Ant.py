import pygame

class Ant(pygame.sprite.Sprite):
    def __init__(self, id, pos, tail_size, ant_color):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.image = pygame.Surface((tail_size, tail_size))
        self.image.fill(ant_color)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def change_position(self, pos):
        self.rect.center = pos
