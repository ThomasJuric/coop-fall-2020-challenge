class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0

    def add(self, num: int):
        self.value = self.value + num
    
    def subtract(self, num: int):
        self.value = self.value - num
        

    def undo(self):
        pass

    def redo(self):
        pass

    def bulk_undo(self, steps: int):
        pass

    def bulk_redo(self, steps: int):
        pass
