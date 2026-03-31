class MinStack:
    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.minstk or val <= self.minstk[-1]:
            self.minstk.append(val)

    def pop(self) -> None:
        if self.stk[-1] == self.minstk[-1]:
            self.stk.pop()
            self.minstk.pop()
        else:
            self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]