import pygame

from core import Board
from display.Pheromones import Pheromones
from display.Ant import Ant

class Mapper():
    def __init__(self, board: Board, tail_size, grass_color, ant_color):
        self.board = board
        self.grass_color = grass_color
        self.tail_size = tail_size
        self.ants = pygame.sprite.Group()
        for ant in self.board.ants:
            position = (ant.position[0] * self.tail_size, ant.position[1] * self.tail_size)
            self.ants.add(Ant(ant.id, position, self.tail_size, ant_color))


    def getPheromones(self):
        cover = Pheromones(self.tail_size, self.board, self.grass_color)
        pheromones = pygame.sprite.Group()
        pheromones.add(cover)
        return pheromones


    def getAnts(self):
        for ant in self.ants:
            pos = self.board.ant(ant.id).position
            ant.change_position((pos[0] * self.tail_size, pos[1] * self.tail_size))
        return self.ants
