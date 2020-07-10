list = []
undoList = []

class EventSourcer():
    # Do not change the signature of any functions
    def __init__(self):
        self.value = 0

    def add(self, num: int):
        self.value = self.value + num
        list.append(num)
    
    def subtract(self, num: int):
        self.value = self.value + (-1 * num)
        list.append((-1 * num))

    def undo(self):
        if(self.value != 0):
            size = len(list)
            undoList.append(list[size-1])
            self.value = self.value - list.pop()
        else:
            pass
        
    def redo(self):
        self.value = self.value + undoList.pop()
        
    def bulk_undo(self, steps: int):
        for x in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for x in range(steps):
            self.redo()

    
