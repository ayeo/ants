import pygame

from core.World import World
from display.Mapper import Mapper

FPS = 30
SIZE = 100
TAIL_SIZE = 5
DELAY = 10
RHO = .01
ANTS = 30

GRASS_COLOR = (252, 233, 88)
ANT_COLOR = (135, 51, 25)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SIZE*TAIL_SIZE, SIZE*TAIL_SIZE))
pygame.display.set_caption("Ants")
clock = pygame.time.Clock()

board = World(SIZE)
board.nest((int(SIZE/2), int(SIZE/2)))
#board.food((10, 10))
for i in range(ANTS):
    board.breed()

mapper = Mapper(board, TAIL_SIZE, GRASS_COLOR, ANT_COLOR)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.update()
    board.evaporate(RHO)
    pheromones = mapper.getPheromones()
    pheromones.update()
    pheromones.draw(screen)

    ants = mapper.getAnts()
    ants.update()
    ants.draw(screen)
    pygame.display.flip()
    pygame.time.delay(DELAY)

pygame.quit()