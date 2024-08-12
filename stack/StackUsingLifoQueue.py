from queue import LifoQueue


class stacklifoqueue:
    def __init__(self):
        self.stack = LifoQueue(maxsize=10)
        self.lst=[]
    def isempty(self):
        return print(f"isempty: {self.stack.empty()}")
    def length(self):
        return print(f"the length of the stack is {self.stack.qsize()}")
    def add(self,value):
        self.stack.put(value)
        self.lst.append(value)
    def remove(self):
        self.lst.pop(-1)
        return print(self.stack.get())
    def isfull(self):
        return print(f"Isfull: {self.stack.full()}")
    def display(self):
        print("LifeQueue doesn't support accessing it.")
        #you either have to get it using the 'get' method.or store it in a list and print it out
        return print(self.lst)
obj = stacklifoqueue()
obj.isempty()
obj.add(2)
obj.add(45)
obj.add(90)
obj.add(74)
obj.add(17)
obj.remove()
obj.isempty()
obj.length()
obj.display()
obj.isfull()