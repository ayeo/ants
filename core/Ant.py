import numpy as np
from core import World

class Ant():
    board: World
    carrying = False

    def __init__(self, id, board: World, position):
        self.id = id
        self.board = board
        self.position = position
        self.breadcrumb = []
        self.moves = ((0, 1), (0, -1), (1, 0), (-1, 0)) # up, down, right, left

    def move_values(self, change):
        position = tuple(np.array(self.position)+change)
        if position in self.breadcrumb:
            return 0

        if position[0] >= self.board.size or position[0] < 0:
            return 0

        if (position in self.board.foods):
            self.carrying = True
            self.breadcrumb = []

        if (position == self.board.nest_position):
            self.carrying = False
            self.breadcrumb = []

        if position[1] >= self.board.size or position[1] < 0:
            return 0

        if (self.carrying):
            return self.board.pheromones[position]
        else:
            return 1

    def change_position(self, move):
        self.board.leave_pheromone(self.position, 1)
        self.breadcrumb.append(self.position)
        self.position = tuple(np.array(self.position) + self.moves[move])


    def update(self):
        moves = []
        for i in range(4):
            moves.append(self.move_values(self.moves[i]))

        if sum(moves) == 0:
            self.breadcrumb = []
            return self.update()

        probabilities = [a / sum(moves) for a in moves]
        move = np.random.choice([z[0] for z in enumerate(moves)], p=probabilities)
        self.change_position(move)
