from collections import deque
import numpy as np
d=deque()
class deque_functions:
    def add(self,val):
        d.append(val)


    def add_left(self,val):
        d.appendleft(val)


    def delete(self):
        print(f"The element {d.pop()} has been deleted.")


    def deleteLeft(self):
        print(f"The element {d.popleft()} has been deleted.")


    def position(self,val):
        print(f"The element is found at the position {d.index(val)}")


    def insert_val(self,val, pos):
        d.insert(pos, val)


    def remove_val(self,val):
        if val in d:
            d.remove(val)
        else:
            print("The value is not present in the deque.")

    def count(self,val):
        print(f"Count of {val} is {d.count(val)}")


    def length(self,d):
        print(len(d))


    def extend(self,arr):
        d.extend(arr)


    def extendleft(self,arr):
        d.extendleft(arr)


    def reverse(self):
        d.reverse()
        print(d)


    def rotate(self,val):
        d.rotate(val)
        print(d)

    def clearall(self,d):
        d.clear()


    def copy(self):
        d.copy()
    def display(self,d):
        print(d)
obj= deque_functions()
while (1):
    option = input("Choose the operation you wish to perform\n1.add\t2.addleft\t3.Delete\t4.deleteleft\t5.position\n6.insert\t7.remove\t8.count\t9.length\t10.extend\n11.entendleft\t12.reverse\t13.rotate\t14.clearall\t15.Display\t16.exit\n")
    match option:
        case '1':
            value = input("enter the value you want to add:\t")
            obj.add(value)
        case '2':
            value = input("enter the value you want to add:\t")
            obj.add_left(value)
        case '3':
            obj.delete()
        case '4':
            obj.deleteLeft()
        case '5':
            value = input("enter the value you want to find the index position:\t")
            obj.position(value)
        case '6':
            val=input("enter the value you want to insert:\t")
            pos=input("enter the  position you want to insert the value:\t")
            obj.insert_val(val,int(pos))
        case '7':
            val=input("enter the value you want to delete\t")
            obj.remove_val(val)
        case '8':
            val=input("enter the value you want to count its occurrence\t")
            obj.count(val)
        case '9':
            obj.length(d)
        case '10':
            arr=np.array(eval(input("enter the array in format eg[2,3,4]\t")))
            arr_str = [str(element) for element in arr]
            obj.extend(arr_str)
        case '11':
            arr = np.array(eval(input("enter the array in format eg[2,3,4]\t")))
            arr_str = [str(element) for element in arr]
            obj.extendleft(arr_str)
        case '12':
            obj.reverse()
        case '13':
            val=int(input("how many value to rotate"))
            obj.rotate(val)
        case '14':
            obj.clearall(d)
        case '15':
            obj.display(d)
        case '16':
            print("Exit.")
            break

