from queue import Queue
class que:
    def __init__(self):
        self.q = Queue(maxsize=5)
        #If the queue already contains 5 items
        # the program will pause execution and wait for another thread to remove an item
        # before it can proceed with adding a new one.

    def __str__(self):
        queue_doc = """
        This is an example of queue.Queue
        1. `q.put(item, block=True, timeout=None)`: Adds an item to the queue; blocks if the queue is full unless `block=False` or a `timeout` is specified.
        2. `q.put_nowait(item)`: Adds an item to the queue without blocking; raises `queue.Full` if the queue is full.
        3. `q.get(block=True, timeout=None)`: Removes and returns an item from the queue; blocks if the queue is empty unless `block=False` or a `timeout` is specified.
        4. `q.get_nowait()`: Removes and returns an item from the queue without blocking; raises `queue.Empty` if the queue is empty.
        5. `q.full()`: Returns `True` if the queue is full, `False` otherwise.
        6. `q.empty()`: Returns `True` if the queue is empty, `False` otherwise.
        7. `q.qsize()`: Returns the approximate number of items in the queue (not reliable in multithreaded environments).
        8. `q.task_done()`: Indicates that a formerly enqueued task is complete; used with `q.join()` for task tracking.
        9. `q.join()`: Blocks until all tasks in the queue have been marked as done with `task_done()`.
        """
        return queue_doc

    def enqueue(self,val):
        self.q.put(val,block=False)

    def dequeue(self):
        print(self.q.get())

    def isempty(self):
        print(self.q.empty())

    def isfull(self):
        print(self.q.full())

obj = que()
print("Select an option\n1.Add\n2.Delete\n3.Isempty\n4.Isfull\n5.Info\n6.exit\n")
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
            print(obj)
        case '6':
            exit(0)