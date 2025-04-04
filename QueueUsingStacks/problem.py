class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        return self.stack[-1] if self.stack else None

    def empty(self):
        return not self.stack

class MyQueue:

    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def push(self, x: int) -> None:
        self.in_stack.push(x)

    def pop(self) -> int:
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.out_stack.empty():
            while not self.in_stack.empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.peek()

    def empty(self) -> bool:
        return self.in_stack.empty() and self.out_stack.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
