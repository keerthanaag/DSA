from collections import deque

stack = deque()


class StackUsingDeque:
    def push(self, val):
        stack.append(val)

    def delete(self):
        print(f"The element deleted from the stack is {stack.pop()}")

    def display(self):
        print(stack)


obj = StackUsingDeque()
while (1):
    option = input("Choose the operation you wish to perform\n1.Push\n2.Pop\n3.Display\n4.Exit\n")
    match option:
        case '1':
            value = input("enter the value you want to add:\t")
            obj.push(value)
        case '2':
            obj.delete()
        case '3':
            obj.display()
        case '4':
            print("Exit.")
            break
