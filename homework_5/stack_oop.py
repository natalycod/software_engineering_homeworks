class Stack:
    def __init__():
        stack_memory = []
    
    def push(self, x):
        self.stack_memory.append(x)
    
    def pop(self):
        x = self.stack_memory[-1]
        self.stack_memory.pop(-1)
        return x

    def back(self):
        return self.stack_memory[-1]