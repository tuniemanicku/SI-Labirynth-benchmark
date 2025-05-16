import tkinter as tk
from Labyrinth import *

import AStar
import AntAlgorithm
import QLearning

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

class MainWindow:
    def __init__(self):
        root = tk.Tk()
        root.title("Projekt SI - Porównanie labiryntów")
        root.geometry(f'{DISPLAY_WIDTH}x{DISPLAY_HEIGHT}')
        root.resizable(False, False)

        #defining widgets
        labyrinthLabel = tk.Canvas(root, background="gray")
        logsLabel1 = tk.Label(root, text="logs1", background="#ffcccc")
        logsLabel2 = tk.Label(root, text="logs2", background="lightgreen")
        logsLabel3 = tk.Label(root, text="logs3", background="lightblue") #could place a button here to go to next step of the current algorithm
        
        qLearningButton = tk.Button(root, text="QLearning", background="gray", command=QLearning.QLearning)

        AStarButton = tk.Button(root, text="A*", background="gray", command=AStar.AStar)

        AntAlgorithmButton = tk.Button(root, text="Ant Algorithm", background="gray", command=AntAlgorithm.AntAlgorithm)

        #defining a grid
        root.columnconfigure(0, weight=2)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(2, weight=1)

        #placing elements
        self.labyrinthType = LabyrinthType.EASY
        self.labyrinth = Labyrinth(self.labyrinthType)
        labyrinthLabel.grid(row=0, rowspan=3, column=0, sticky="news")
        logsLabel1.grid(row=0, column=1, sticky="news")
        logsLabel2.grid(row=1, column=1, sticky="news")
        logsLabel3.grid(row=2, column=1, sticky="news")
        step = DISPLAY_HEIGHT//LABYRINTH_SIZE
        for y in range(LABYRINTH_SIZE):
            for x in range(LABYRINTH_SIZE):
                color = "white" if self.labyrinth.board[y][x] == 1 else "red"
                labyrinthLabel.create_rectangle(x*step,y*step,(x+1)*step,(y+1)*step, fill=color)

        qLearningButton.grid(row=0, column=2, sticky="news")
        AStarButton.grid(row=1, column=2, sticky="news")
        AntAlgorithmButton.grid(row=2, column=2, sticky="news")
        self.root = root

    def mainLoop(self):
        self.root.mainloop()
    
    def updateBoard(self,labyrinth):
        pass

    def resetBoard(self, labyrinthType=LabyrinthType.EASY):
        self.labyrinth = Labyrinth(labyrinthType)
        self.updateBoard(self.labyrinth)