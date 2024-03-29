class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.length = maxSize

    def push(self, x: int) -> None:
        if self.length != len(self.stack):
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k , len(self.stack))):
            self.stack[i] += val 


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
