from queue import LifoQueue
class queue:
    def __init__(self,siz):
        self.q = LifoQueue(maxsize=siz)
        self.temp = LifoQueue(maxsize=siz)
    def __str__(self):
        return "This is a LIFO queue"
    def enqueue(self,val):
        if self.q.full():
            print("The queue is full")
        else:
            self.q.put(val,timeout=False)
    def dequeue(self):
        if self.q.empty():
            print("The queue is empty")
        else:
            while self.q.qsize():
                ex = self.q.get()
                self.temp.put(ex)
            remove = self.temp.get()
            while self.temp.qsize():
                self.q.put(self.temp.get())
            print(remove)

    def is_empty(self):
        print(self.q.empty())
    def is_full(self):
        print(self.q.full())
    def size(self):
        print(self.q.qsize())
siz = int(input("enter max size of queue:\t"))
obj = queue(siz)
print("Select an option\n1.Add\n2.Delete\n3.Isempty\n4.IsFull\n5.size\n6.Info\n7.exit\n")
while(1):
    option = input()
    match option:
        case '1':
            value = input("enter the value you want to add:\t")
            obj.enqueue(value)
        case '2':
            obj.dequeue()
        case '3':
            obj.is_empty()
        case '4':
            obj.is_full()
        case '5':
            obj.size()
        case '6':
            print(obj)
        case '7':
            exit(0)
        