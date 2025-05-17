import tkinter as tk
from Labyrinth import *
from copy import deepcopy

from Algorithm import Algorithm
from AStar import AStar
from AntAlgorithm import AntAlgorithm
from QLearning import QLearning

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

class WallModificationException(Exception):
    pass

class MainWindow:
    def __init__(self):
        root = tk.Tk()
        root.title("Projekt SI - Porównanie labiryntów")
        root.geometry(f'{DISPLAY_WIDTH}x{DISPLAY_HEIGHT}')
        root.resizable(False, False)

        #defining widgets
        labyrinthLabel = tk.Canvas(root, background="gray")
        logsLabel1 = tk.Label(root, text="logs1", background="#ffcccc")
        self.logs1 = []
        logsLabel2 = tk.Label(root, text="logs2", background="lightgreen")
        self.logs2 = []
        #logsLabel3 = tk.Label(root, text="logs3", background="lightblue") #could place a button here to go to next step of the current algorithm
        controlPanel = tk.Label(root, bg="white")

        #defining algorithm buttons
        self.algorithm = Algorithm(self)
        qLearningButton = tk.Button(root, text="QLearning", background="gray", command=lambda alg="q": self.setAlgorithm(alg))

        AStarButton = tk.Button(root, text="A*", background="gray", command=lambda alg="a*": self.setAlgorithm(alg))

        AntAlgorithmButton = tk.Button(root, text="Ant Algorithm", background="gray", command=lambda alg="ant": self.setAlgorithm(alg))

        #defining control panel buttons
        nextButton = tk.Button(controlPanel, text="Next step")
        nextButton.pack(side="bottom")
        resetButton = tk.Button(controlPanel, text="Reset board", command=self.resetBoard)
        resetButton.pack(side="bottom")
        self.nextButton = nextButton

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
        self.originalLabyrinth = deepcopy(self.labyrinth)
        labyrinthLabel.grid(row=0, rowspan=3, column=0, sticky="news")
        logsLabel1.grid(row=0, column=1, sticky="new")
        logsLabel2.grid(row=1, column=1, sticky="new")
        controlPanel.grid(row=2, column=1, sticky="news")
        #logsLabel3.grid(row=2, column=1, sticky="news")

        step = DISPLAY_HEIGHT//LABYRINTH_SIZE
        self.step = step
        for y in range(LABYRINTH_SIZE):
            for x in range(LABYRINTH_SIZE):
                color = "white" if self.labyrinth.board[y][x] == 0 else "red"
                labyrinthLabel.create_rectangle(x*step,y*step,(x+1)*step,(y+1)*step, fill=color)

        qLearningButton.grid(row=0, column=2, sticky="news")
        AStarButton.grid(row=1, column=2, sticky="news")
        AntAlgorithmButton.grid(row=2, column=2, sticky="news")
        self.root = root
        self.logs1Label = logsLabel1
        self.logs2Label = logsLabel2
        self.canvas = labyrinthLabel

    def setAlgorithm(self, alg="q"):
        if alg == "q":
            self.algorithm = QLearning(self)
        elif alg == "ant":
            self.algorithm = AntAlgorithm(self)
        else:
            self.algorithm = AStar(self)
        self.nextButton.config(command=self.algorithm.nextStep)
    
    def mainLoop(self):
        self.root.mainloop()
    
    def updateBoard(self,x,y,color="blue"):
        if self.labyrinth.board[y][x] == 1:
            raise WallModificationException("You cannot modify wall colors")
        self.canvas.create_rectangle(x*self.step,y*self.step,(x+1)*self.step,(y+1)*self.step, fill=color)

    def updateLogs1(self, newString="default"):
        if len(self.logs1) > 6:
            self.logs1.pop(0)
        self.logs1.append(newString)
        newText = "logs1\n" + "\n".join(self.logs1)
        self.logs1Label.config(text=newText)

    def updateLogs2(self, newString="default"):
        if len(self.logs2) > 6:
            self.logs2.pop(0)
        self.logs2.append(newString)
        newText = "logs2\n" + "\n".join(self.logs2)
        self.logs2Label.config(text=newText)
    
    def resetBoard(self, labyrinthType=LabyrinthType.EASY):
        self.labyrinth = deepcopy(self.originalLabyrinth)
        for y in range(LABYRINTH_SIZE):
            for x in range(LABYRINTH_SIZE):
                color = "white" if self.labyrinth.board[y][x] == 0 else "red"
                self.canvas.create_rectangle(x*self.step,y*self.step,(x+1)*self.step,(y+1)*self.step, fill=color)