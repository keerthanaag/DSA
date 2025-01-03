class queue:
    def __init__(self,siz):
        self.front = -1
        self.rear = -1
        self.lstqueue =[]
        self.size = siz
    def enqueue(self,value):
        if abs(self.rear-self.front) == self.size - 1:
            print(self.rear,self.size-1)
            print("Overflow")
        else:
            if len(self.lstqueue) == 0:
                self.front +=1
            self.rear += 1
            self.lstqueue.append(value)
            print(f"The {value} is added to the queue")
    def dequeue(self):
        if self.rear < self.front:
            print("Underflow")
        else:
            print(f"The deleted value is {self.lstqueue[self.front]}")
            self.front += 1
    def isempty(self):
        if self.rear < self.front or self.front == -1:
            print("True")
        else:
            print("False")
    def isfull(self):
        if abs(self.rear-self.front) == self.size - 1:
            print(self.rear, self.size)
            print("True")
        else:
            print("False")
    def peek(self):
        if self.rear == self.front:
            print("Queue is EMPTY")
        else:
            print(f"The Peak value is {self.lstqueue[self.rear]}")
    def display(self):
        print(self.lstqueue[self.front:])
obj = queue(10)
print("Size of the array is 10")
print("Select an option\n1.Add\n2.Delete\n3.Isempty\n4.Isfull\n5.Peek\n6.display\n7.exit\n")
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
        case '6':
            exit(0)



