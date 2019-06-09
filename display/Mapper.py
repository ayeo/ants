import pygame

from core import World
from display.Board import Board
from display.AntSprite import AntSprite

class Mapper():
    def __init__(self, board: World, tail_size, grass_color, ant_color, nest_color, food_color):
        self.board = board
        self.grass_color = grass_color
        self.nest_color = nest_color
        self.food_color = food_color
        self.tail_size = tail_size
        self.ants = pygame.sprite.Group()
        for ant in self.board.ants:
            position = (ant.position[0] * self.tail_size, ant.position[1] * self.tail_size)
            self.ants.add(AntSprite(ant, position, self.tail_size, ant_color))


    def getPheromones(self):
        cover = Board(self.tail_size, self.board, self.grass_color, self.nest_color, self.food_color)
        pheromones = pygame.sprite.Group()
        pheromones.add(cover)
        return pheromones


    def getAnts(self):
        for ant in self.ants:
            pos = self.board.ant(ant.id).position
            ant.change_position((pos[0] * self.tail_size, pos[1] * self.tail_size))
        return self.ants
