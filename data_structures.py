# Design min stack
class MinStack:
    def __init__(self):
        self.stack: list[int] = []
        self.min_values_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        min_value = val if not self.min_values_stack else min(val, self.min_values_stack[-1])
        self.min_values_stack.append(min_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_values_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values_stack[-1]


min_stack: MinStack = MinStack()
min_stack.push(1)
min_stack.push(2)
min_stack.push(0)
print(min_stack.getMin())  # return 0
min_stack.pop()
print(min_stack.top())  # return 2
print(min_stack.getMin())  # return 1

print(min_stack.stack)
print(min_stack.min_values_stack)
