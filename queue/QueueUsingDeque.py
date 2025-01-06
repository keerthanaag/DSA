from collections import deque
class queueusingdeque:
    def __init__(self):
        self.d = deque([],maxlen=10)
    def __str__(self):
        return "Size of the array is 10.\nIf the value is added incase of Overflow,the first element is removed and then the value is added."
    def enqueue(self,value):
        self.d.append(value)
        print(f"The value {value} has been added.")
    def dequeue(self):
        if len(self.d) == 0:
            print("Queue is empty.")
        else:
            val = self.d.popleft()
            print(f"The value {val} has been removed.")
    def isempty(self):
        if len(self.d) == 0:
            print(True)
        else:
            print(False)
    def isfull(self):
        print(len(self.d) == self.d.maxlen)
    def peek(self):
        print(self.d[0])
    def display(self):
        print(self.d)
    def info(self):
        print(self.d)
obj = queueusingdeque()
print("Select an option\n1.Add\n2.Delete\n3.Isempty\n4.Isfull\n5.Peek\n6.display\n7.exit\n8.Info\n")
while(1):
    option = input()
    match option:
        case '1':
            value = input("enter the value you want to add:\t")
            obj.enqueue(value)
        case '2':
            obj.dequeue()
        case '3':
            obj.isempty()
        case '4':
            obj.isfull()
        case '5':
            obj.peek()
        case '6':
            obj.display()
        case '7':
            exit(0)
        case '8':
            print(obj)
