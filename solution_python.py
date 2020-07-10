list = []

class EventSourcer():
    # Do not change the signature of any functions
    def __init__(self):
        self.value = 0

    def add(self, num: int):
        self.value = self.value + num
        list.append(num)
    
    def subtract(self, num: int):
        self.value = self.value + (-1 * num)
        list.append(-1 * num)

    def undo(self):
        self.value = self.value - list.pop()
        
    def redo(self):
        pass

    def bulk_undo(self, steps: int):
        for x in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        pass

    
