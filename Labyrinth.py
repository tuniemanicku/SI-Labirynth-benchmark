from enum import Enum
import numpy as np
from Utilities import Point

LABYRINTH_SIZE = 30

class LabyrinthType(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

class Labyrinth:
    def __init__(self, type=LabyrinthType.EASY):
        self.board = np.random.randint(2, size=(LABYRINTH_SIZE,LABYRINTH_SIZE), dtype=int)
        self.walls = np.random.randint(2, size=(LABYRINTH_SIZE+1,LABYRINTH_SIZE+1), dtype=int)
        self.exit = Point(x=LABYRINTH_SIZE-1, y=LABYRINTH_SIZE-1)

