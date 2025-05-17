from Algorithm import Algorithm

class AntAlgorithm(Algorithm):
    def __init__(self, window):
        super().__init__(window)
        print("Hello from Ant algorithm file")
    def nextStep(self):
        self.window.updateBoard(1,1)
        self.window.updateLogs1("Hello from Ant algorithm file")