#STACK IMPLEMENTATION IN PYTHON
#jgkattikatt@gmail.com

class StackException(Exception):
    """stack exception class
    """ 
    pass


class Stack:
    """stack implementation
       interfaces : push, pop, isEmpty, size
       implementation : list data type
    """

    def __init__(self):
        """instantiates a stack instance
        """
        self._stack_items = []

    def push(self, item=None):
        """push() - inserts item to the top of the stack
           args : item
           on failure : StackException()
        """
        if item:
            self._stack_items.append(item)
        else:
            raise StackException('stack element cannot be an empty string')    

    def pop(self):
        """pop() - returns last inserted item from the stack
           args : None
           return : item
           on failure : StackException()
        """
        if not self.is_empty():
            return self._stack_items.pop()
        else:
            raise StackException('Pop operation not supported on an empty stack')

    def peek(self):
        """peek() - returns last inserted item without removing it from the stack
           args : None
           return : item
           on failure : StackException()
        """
        if not self.is_empty():
            return self._stack_items[-1]
        else:
            raise StackException('Peek operation not supported on an empty stack')

    def is_empty(self):
        """is_empty() - returns True if stack is empty, else False
           args : None
           return : bool
        """
        return self._stack_items == []

    def size(self):
        """size() - returns size of the stack
           args : None
           return : integer
        """
        return len(self._stack_items)

    def __repr__(self):
        """__repr__() - returns the current stack in string format
           args : None
           return : string
        """
        return str(self._stack_items)


if __name__ == '__main__':
    stack_obj = Stack()
    stack_obj.push(1)
    stack_obj.push(2)
    print stack_obj
    print stack_obj.pop()
    print stack_obj.is_empty()
    print stack_obj.size()
    print stack_obj
