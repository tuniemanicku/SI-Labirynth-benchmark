from Algorithm import Algorithm

class AStar(Algorithm):
    def __init__(self, window):
        super().__init__(window)
        print("Hello from A* file")
    def nextStep(self):
        self.window.updateBoard(1,2)
        self.window.updateLogs1("Hello from A* file")