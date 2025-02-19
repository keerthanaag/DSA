class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertatbegin(self):
        self.value = int(input("Enter the value to be added"))
        if self.head == None:
            self.head = Node(self.value)
            self.size += 1
        else:
            newnode = Node(self.value)
            newnode.next = self.head
            self.head = newnode
            self.size += 1
        print(f"The {self.value} is inserted")

    def insertatend(self):
        self.value = int(input("Enter the value to be added"))
        newnode = Node(self.value)
        curnode = self.head
        while curnode.next :
            curnode = curnode.next
        curnode.next = newnode

    def insertatindex(self):
        self.index = int(input("Enter the index in which he value should be added"))
        if self.index == 0:
            self.insertatbegin()
        else:
            self.value = int(input("Enter the value to be added"))
            curnode = self.head
            pos = 0
            newnode = Node(self.value)
            while curnode.next != None and pos+1 != self.index:
                curnode = curnode.next
                pos += 1
            newnode.next = curnode.next
            curnode.next = newnode
    def update(self):
        self.value = int(input("Enter the value to be added"))
        self.index = int(input("Enter the index in which he value should be added"))
        curnode = self.head
        pos = 0
        while curnode.next and self.index != pos:
            curnode = curnode.next
            pos += 1
        curnode.data = self.value

    def deleteatbegin(self):
        if self.head == None:
            print("no node in linkedlist")
        self.head = self.head.next
        self.size -= 1

    def deleteatend(self):
        if self.head == None:
            print("no node in linkedlist")
        else:
            cur = self.head
            while cur.next and cur.next.next:
                cur = cur.next
            cur.next = None
            self.size -= 1

    def deleteatmiddle(self):
        if self.head == None:
            print("no node in linkedlist")
        else:
            self.index = int(input("Enter the index in which he value should be deleted"))
            cur = self.head
            pos = 0
            while cur.next and pos+1 != self.index:
                cur = cur.next
                pos += 1
            cur.next = cur.next.next

    def deletewithdata(self):
        if self.head == None:
            print("no node in linkedlist")
        else:
            self.value = int(input("Enter the value of the node to be deleted"))
            cur = self.head
            if cur.data == self.value:
                self.head = self.head.next
                return 0
            while cur.next and cur.next.data != self.value:
                cur = cur.next
            cur.next = cur.next.next

    def length(self):
        print(f"the size is {self.size}")
    def display(self):
        cur = self.head
        while cur.next:
            print(f"{cur.data}->",end=" ")
            cur = cur.next
        print(cur.data)

obj = linkedlist()
obj.insertatbegin()
obj.insertatbegin()
obj.length()
obj.display()
obj.insertatbegin()
obj.insertatindex()
obj.insertatend()
obj.insertatindex()
obj.display()
obj.update()
obj.deleteatend()
obj.display()
obj.deleteatmiddle()
obj.display()
obj.deleteatbegin()
obj.display()
obj.deletewithdata()
obj.display()




