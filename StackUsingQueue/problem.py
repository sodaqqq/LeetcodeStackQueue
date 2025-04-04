class Queue: 
    
    def __init__(self):
        self.queue = []
    
    def push(self, x):
        self.queue.append(x)
    
    def peek(self):
        return self.queue[0] if self.queue else None
    
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def empty(self):
        return not self.queue


class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)
        for _ in range(len(self.queue.queue) - 1):
            self.queue.push(self.queue.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
