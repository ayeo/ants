import pygame
import math

from colorsys import rgb_to_hls, hls_to_rgb
from core.Board import Board

class Pheromones(pygame.sprite.Sprite):
    def __init__(self, tail_size, board: Board):
        pygame.sprite.Sprite.__init__(self)
        self.board = board
        self.tail_size = tail_size
        self.image = pygame.Surface((tail_size * board.size, tail_size * board.size))
        self.image.fill((100, 255, 100))
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

        c = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1]
        self.colors = []
        base_color = (100, 255, 100)
        for x in range(10):
            self.colors.append(self.adjust_color_lightness(base_color, c[x]))


    def update(self, *args):
        for x, rows in enumerate(self.board.pheromones):
            for y, value in enumerate(rows):
                if value <= 0.1:
                    continue
                value = min(value, 9)
                color = self.colors[math.floor(value)]
                ts = self.tail_size
                pygame.draw.rect(self.image, color, (x*ts-math.floor(ts/2), y*ts-math.floor(ts/2), ts, ts))


    def adjust_color_lightness(self, color, factor):
        h, l, s = rgb_to_hls(color[0]/255.0, color[1]/255.0, color[2]/255.0)
        l = max(min(l * factor, 1.0), 0.0)
        r, g, b = hls_to_rgb(h, l, s)
        return (int(r*255), int(g*255), int(b*255))