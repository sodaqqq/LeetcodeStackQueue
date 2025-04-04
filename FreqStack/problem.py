class FreqStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        freq = {}
        for val in self.stack:
            freq[val] = freq.get(val, 0) + 1

        max_freq = max(freq.values())
    
        for i in range(len(self.stack) - 1, -1, -1):
            val = self.stack[i]
            if freq[val] == max_freq:
                self.stack.pop(i)
                return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
