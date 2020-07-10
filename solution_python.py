#Create lists, one for main list and one to keep track of what has been popped off
list = []
undoList = []

class EventSourcer():
    # Do not change the signature of any functions
    def __init__(self):
        self.value = 0

    def add(self, num: int):
        # Add the value to the overall, and add int to list
        self.value = self.value + num
        list.append(num)
    
    def subtract(self, num: int):
        # Subtract the value from the overall value, and add the negative number to the list
        self.value = self.value + (-1 * num)
        list.append((-1 * num))

    def undo(self):
        # Check if something has been sent as a parameter
        if(self.value != 0):
            # Pop the first object from the list, and subtract it from the overall value
            size = len(list)
            undoList.append(list[size-1])
            self.value = self.value - list.pop()
        else:
            pass
        
    def redo(self):
        # Check if there is a parameter
        if(self.value != 0):
            # Add the last item from the undoList onto the original list, as it was the last item popped off
            self.value = self.value + undoList.pop()
        else:
            pass
    # Loop through
    def bulk_undo(self, steps: int):
        for x in range(steps):
                self.undo()
    # Loop through previous functions
    def bulk_redo(self, steps: int):
        for x in range(steps):
            if (self.value != 25):
                self.redo()

    
