#QUEUE IMPLEMENTATION IN PYTHON
#jgkattikatt@gmail.com

class QueueException(Exception):
    """queue exception class
    """ 
    pass


class Queue:
    """queue implementation
       interfaces : enqueue, dequeue, peek, isEmpty, size
       implementation : list data type
    """

    def __init__(self):
        """instantiates a queue instance
        """
        self._queue_items = []

    def enqueue(self, item=None):
        """enqueue() - inserts item to the queue
           args : item
           on failure : QueueException()
        """
        if item:
            self._queue_items.insert(0, item)
        else:
            raise QueueException('queue element cannot be an empty string')    

    def dequeue(self):
        """dequeue() - returns first inserted item from the queue
           args : None
           return : item
           on failure : QueueException()
        """
        if not self.is_empty():
            return self._queue_items.pop()
        else:
            raise QueueException('dequeue operation not supported on an empty queue')

    def peek(self):
        """peek() - returns last inserted item without removing it from the queue
           args : None
           return : item
           on failure : QueueException()
        """
        if not self.is_empty():
            return self._queue_items[-1]
        else:
            raise QueueException('Peek operation not supported on an empty queue')

    def is_empty(self):
        """is_empty() - returns True if queue is empty, else False
           args : None
           return : bool
        """
        return self._queue_items == []

    def size(self):
        """size() - returns size of the queue
           args : None
           return : integer
        """
        return len(self._queue_items)

    def __repr__(self):
        """__repr__() - returns the current queue in string format
           args : None
           return : string
        """
        return str(self._queue_items)


if __name__ == '__main__':
    queue_obj = Queue()
    queue_obj.enqueue(1)
    queue_obj.enqueue(2)
    queue_obj.enqueue(3)
    print queue_obj
    print queue_obj.dequeue()
    print queue_obj.peek()
    print queue_obj.is_empty()
    print queue_obj.size()
    print queue_obj
