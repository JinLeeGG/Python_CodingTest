class Stack:
    def __init__(self, size):
        self.stack = []
        self.maxsize = size

    def isFull(self):
        return len(self.stack) == self.maxsize

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        if self.isFull():
            print('Full')
        else:
            self.stack.append(item)
    
    def pop(self):
        if self.isEmpty():
            print('empty')
            return None
        else:
            return self.stack.pop()


s = Stack(10)
s.push(10)
s.push(3213)
print(s.stack)
s.pop()
print(s.stack)
