from Algorithm import Algorithm

#należy napisać algorytm by był przystosowany do wywołania konstruktora i nextStep
#klasa window ma pola:  labyrinth.board[y][x], gdzie 1 - ściana, 0 - pole
#                       labyrinth.exit, które ma pola exit.x i exit.y
#                       exit defaultowo znajduje się w prawym-górnym rogu czyli (LABYRINTH_SIZE-1, 0) LABYRINTH_SIZE znajduje się w Labyrinth.py
#                       start defaultowo uznaje się za (0, LABYRINTH_SIZE-1)
#                       labirynt wyświetalny w oknie jest wczytywany zawsze z "save.txt" można to sparametryzować później

class AntAlgorithm(Algorithm):
    def __init__(self, window):
        super().__init__(window)
        print("Hello from Ant algorithm file")
    def nextStep(self):
        self.window.updateBoard(x=1,y=1) #w ten sposób kolorujemy kratki (0,0) jest w lewym-górnym rogu
        self.window.updateLogs1("Hello from Ant algorithm file") #tak dodajemy wpis do logów