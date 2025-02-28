class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queueUsinglinkedlist:
    def __init__(self,size):
        self.head = None
        self.maxsize = size

    def enqueue(self):
        cursiz = self.length()
        if cursiz == self.maxsize:
            print("Overflow")
            return 0
        self.value = int(input("Enter the value to be added:\t"))
        if self.head == None:
            self.head = Node(self.value)

        else:
            newnode = Node(self.value)
            newnode.next = self.head
            self.head = newnode
        self.display()

    def dequeue(self):
        if self.head == None:
            print("Underflow")
        else:
            cur = self.head
            if cur.next == None:
                print(f"{cur.data} deleted")
                self.head =None
            else:
                while cur.next != None and cur.next.next != None:
                    cur = cur.next
                print(f"{cur.next.data} deleted")
                cur.next = None

    def peek(self):
        if self.head == None:
            print("No node in linked list")
        else:
            print("the peak element is: ",self.head.data)

    def isempty(self):
        if self.head == None:
            print("isempty: ",True)
        else:
            print("isempty: ",False)

    def isfull(self):
        if self.length() == self.maxsize:
            print("isfull: ",True)
        else:
            print("isfull: ",False)

    def length(self):
        s = 0
        cur = self.head
        if self.head == None:
            return 0
        while cur.next != None:
            cur = cur.next
            s += 1
        return s+1

    def display(self):
        if self.head == None:
            print("the stack is empty")
            return 0
        cur = self.head
        while cur.next:
            print(f"{cur.data}->",end=" ")
            cur = cur.next
        print(cur.data)

obj = queueUsinglinkedlist(5)
print("Choose the operation you wish to perform\n1.Push\n2.Pop\n3.Display\n4.Peek\n5.length\n6.Isempty\n7.Isfull\n8.Exit\n")
while (1):
    option = input()
    match option:
        case '1':
            obj.enqueue()
        case '2':
            obj.dequeue()
        case '3':
            obj.display()
        case '4':
            obj.peek()
        case '5':
            print(f"the length is {obj.length()}")
        case '6':
            obj.isempty()
        case '7':
            obj.isfull()
        case '8':
            print("Exit.")
            break

