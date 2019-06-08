import numpy as np

from core.Ant import Ant

class Board():
    ants = []

    def __init__(self, size):
        self.pheromones = np.full((size, size), 0.1, dtype=float)
        self.size = size


    def nest(self, position: (int, int)):
        self.nest_position = position


    def breed(self) -> Ant:
        ant = Ant(len(self.ants), self, self.nest_position)
        self.ants.append(ant)
        return ant

    def ant(self, id) -> Ant:
        return self.ants[id]


    def leave_pheromone(self, pos, quantity):
        if pos[0] >= self.size or pos[0] < 0:
            return

        if pos[1] >= self.size or pos[1] < 0:
            return

        self.pheromones[pos] = self.pheromones[pos] + quantity


    def evaporate(self, quantity):
        self.pheromones = self.pheromones - quantity
        self.pheromones = np.round(self.pheromones, 2)
        self.pheromones = np.array([[max(0.1, x) for x in y] for y in self.pheromones])



    def update(self):
        for ant in self.ants:
            ant.update()
