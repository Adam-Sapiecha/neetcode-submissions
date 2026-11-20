class MinStack:

    def __init__(self):
        self.stos = []
        self.minimum = []
    def push(self, val: int) -> None:
        if self.minimum and val <= self.minimum[-1]:
            self.minimum.append(val)
        elif len(self.minimum) == 0:
            self.minimum.append(val)
        self.stos.append(val)
    def pop(self) -> None:
        if self.stos[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.stos.pop()
    def top(self) -> int:
        return self.stos[-1]
    def getMin(self) -> int:
        return self.minimum[-1]
