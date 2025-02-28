class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stckUsinglinkedlist:
    def __init__(self,size):
        self.head = None
        self.maxsize = size

    def push(self):
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

    def pop(self):
        if self.head == None:
            print("Underflow")
            return 0
        print(f"{self.head.data} deleted")
        self.head = self.head.next


    def peek(self):
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

obj = stckUsinglinkedlist(5)
print("Choose the operation you wish to perform\n1.Push\n2.Pop\n3.Display\n4.length\n5.Isempty\n6.Isfull\n7.Exit\n")
while (1):
    option = input()
    match option:
        case '1':
            obj.push()
        case '2':
            obj.pop()
        case '3':
            obj.display()
        case '4':
            print(f"the length is {obj.length()}")
        case '5':
            obj.isempty()
        case '6':
            obj.isfull()
        case '7':
            print("Exit.")
            break

