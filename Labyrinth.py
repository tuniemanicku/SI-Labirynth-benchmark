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
        loadedBoard = np.zeros(shape=(LABYRINTH_SIZE,LABYRINTH_SIZE), dtype=int)
        try:
            with open("save.txt", "r") as f:
                lines = f.readlines()
                for y, line in enumerate(lines):
                    values = line.strip().split()
                    for x, val in enumerate(values):
                        value = int(val)
                        loadedBoard[y][x] = value
        except FileNotFoundError:
            print("save.txt not found.")
        self.board = loadedBoard
        self.exit = Point(x=LABYRINTH_SIZE-1, y=LABYRINTH_SIZE-1)

