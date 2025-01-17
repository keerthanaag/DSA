from queue import PriorityQueue

class priority:
    def __init__(self):
        self.q = PriorityQueue(maxsize=5)

    def __str__(self):
        return """
         PriorityQueue Methods Documentation
        
        - The `queue.PriorityQueue` provides the following methods:
          1. `put(item, block=True, timeout=None)`: Adds an item with priority, blocking if necessary or raising `queue.Full` after timeout.
          2. `get(block=True, timeout=None)`: Retrieves and removes the lowest-priority item, blocking if empty or raising `queue.Empty` after timeout.
          3. `qsize()`: Returns the approximate number of items in the queue (not reliable in multi-threaded environments).
          4. `empty()`: Checks if the queue is empty, returning `True` if it is.
          5. `full()`: Checks if the queue is full, returning `True` if it is.
          6. `task_done()`: Signals completion of a task retrieved by `get()`, useful for task tracking in producer-consumer scenarios.
          7. `join()`: Blocks until all `put()` tasks have been marked as done with `task_done()`.
        """
    def enqueue(self):
        task = input("Enter the task:\t")
        prior = int(input("Priority:\t"))
        self.q.put((prior,task),block=True)

    def dequeue(self):
        p,t = self.q.get()
        print(f"Priority: {p}\nTask: {t}")
    def is_empty(self):
        print(self.q.empty())
    def is_full(self):
        print(self.q.full())
    def size(self):
        print(self.q.qsize())
obj = priority()
print("Select an option\n1.Add\n2.Delete\n3.Isempty\n4.Isfull\n5.Size\n6.Info\n7.exit\n")
while(1):
    option = input()
    match option:
        case '1':
            obj.enqueue()
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