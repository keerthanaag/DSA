class stackExample:
    def __init__(self):
        self.TOS = -1
        self.stack = []

    def isempty(self):
        if self.TOS == -1:
            print("Stack is empty")
            return True
        print("Stack is not empty")
        return False

    def isfull(self):
        if self.TOS == len(self.stack):
            return True
        return False

    def push(self, value):
        if self.isfull():
            print("Stack is full.Element cant be added")
        else:
            self.stack.append(value)
            self.TOS += 1

    def pop(self):
        if self.isempty():
            print("Stack is empty.So element cant be popped")
        else:
            self.peek()
            self.stack.pop(self.TOS)
            self.TOS -= 1

    def peek(self):
        print(f"the peek element is {self.stack[self.TOS]}")

    def display(self):
        for i in range(len(self.stack)):
            print(self.stack[i])


obj = stackExample()
obj.push(21)
obj.push(2)
obj.push(7)
obj.push(80)
obj.isempty()
obj.pop()
obj.display()
