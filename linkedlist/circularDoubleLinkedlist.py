class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
        self.prev = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def insertatbegin(self):
        self.value = int(input("Enter the value to be added"))
        newnode = Node(self.value)
        if self.head == None:
            print("entered")
            self.head = newnode
            newnode.prev = newnode
            newnode.next = newnode
            self.size += 1
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newnode
            newnode.prev = cur
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.size += 1
        print(f"The {self.value} is inserted")

    def insertatend(self):
        self.value = int(input("Enter the value to be added"))
        newnode = Node(self.value)
        curnode = self.head
        while curnode.next != self.head:
            curnode = curnode.next
        newnode.prev = curnode
        newnode.next = curnode.next
        curnode.next.prev = newnode
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
            while curnode.next != self.head and pos+1 != self.index:
                curnode = curnode.next
                pos += 1
            newnode.next = curnode.next
            curnode.next.prev = newnode
            curnode.next = newnode
            newnode.prev = curnode
    def update(self):
        self.value = int(input("Enter the value to be added"))
        self.index = int(input("Enter the index in which he value should be added"))
        curnode = self.head
        pos = 0
        if self.index == pos:
            self.head.data = self.value
            return ""
        while curnode.next and self.index != pos+1:
            curnode = curnode.next
            pos += 1
        curnode.next.data = self.value

    def deleteatbegin(self):
        if self.head == self.head.next:
            self.head = None
            self.size -= 1
            return ""
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = self.head.next
        self.head.next.prev = cur
        self.head = self.head.next
        self.size -= 1

    def deleteatend(self):
        if self.head == None:
            print("no node in linkedlist")
        else:
            cur = self.head
            while cur.next != self.head and cur.next.next != self.head:
                cur = cur.next
            cur.next = self.head
            self.head.prev = cur
            self.size -= 1

    def deleteatmiddle(self):
        if self.head == None:
            print("no node in linkedlist")
        else:
            self.index = int(input("Enter the index in which he value should be deleted"))
            if self.index == self.size-1:
                self.deleteatend()
                self.size -=1
                return ""
            cur = self.head
            pos = 0
            while cur.next != self.head and pos != self.index:
                cur = cur.next
                pos += 1
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            self.size -= 1

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
            self.size -= 1

    def length(self):
        print(f"the size is {self.size}")
    def display(self):
        if self.head == None:
            return None
        cur = self.head
        while cur.next != self.head:
            print(f"{cur.data}->",end=" ")
            cur = cur.next
        print(cur.data)

obj = linkedlist()
obj.insertatbegin()
obj.display()
obj.insertatbegin()
obj.display()
obj.insertatindex()
obj.display()
obj.insertatindex()
obj.display()
obj.insertatindex()
obj.display()
obj.deleteatmiddle()
obj.display()
obj.insertatend()
obj.display()
obj.insertatbegin()
obj.display()
obj.update()
obj.display()
obj.insertatbegin()
obj.display()
obj.update()
obj.display()
obj.deleteatbegin()
obj.length()
obj.display()
obj.deletewithdata()
obj.display()




