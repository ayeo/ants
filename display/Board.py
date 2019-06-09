import pygame
import math

from colorsys import rgb_to_hls, hls_to_rgb
from core.World import World

class Board(pygame.sprite.Sprite):
    def __init__(self, tail_size, board: World, base_color, nest_color, food_color):
        pygame.sprite.Sprite.__init__(self)
        self.board = board
        self.nest_color = nest_color
        self.food_color = food_color
        self.tail_size = tail_size
        self.image = pygame.Surface((tail_size * board.size, tail_size * board.size))
        self.image.fill(base_color)
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0

        c = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.15, 0.1]
        self.colors = []
        for x in range(10):
            self.colors.append(self.adjust_color_lightness(base_color, c[x]))


    def update(self, *args):
        ts = self.tail_size
        # draw pheromones A
        for x, rows in enumerate(self.board.pheromones):
            for y, value in enumerate(rows):
                if value <= 0.1:
                    continue
                value = min(value, 9)
                color = self.colors[math.floor(value)]
                pygame.draw.rect(self.image, color, (x*ts-math.floor(ts/2), y*ts-math.floor(ts/2), ts, ts))

        # draw nest
        ts = self.tail_size
        rect = (self.board.nest_position[0] * ts, self.board.nest_position[0] * ts, ts, ts)
        pygame.draw.rect(self.image, self.nest_color, rect)

        # draw food
        for food in self.board.foods:
            rect = (food[0] * ts, food[0] * ts, ts, ts)
            pygame.draw.rect(self.image, self.food_color, rect)


    def adjust_color_lightness(self, color, factor):
        h, l, s = rgb_to_hls(color[0]/255.0, color[1]/255.0, color[2]/255.0)
        l = max(min(l * factor, 1.0), 0.0)
        r, g, b = hls_to_rgb(h, l, s)
        return (int(r*255), int(g*255), int(b*255))