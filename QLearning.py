from Algorithm import Algorithm

class QLearning(Algorithm):
    def __init__(self, window):
        super().__init__(window)
        print("Hello from QLearning file")
    def nextStep(self):
        self.window.updateBoard(1,3)
        self.window.updateLogs1("Hello from QLearning file")