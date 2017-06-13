#SINGLE LINKED LIST IMPLEMENTATION IN PYTHON
#jgkattikatt@gmail.com


class SingleLinkedListException(Exception):
    """single linked list exception class
    """
    pass


class Node:
    """Linked list individual node implementation
       interfaces : get_item, set_item, set_next, get_next
    """

    def __init__(self, item=None):
        """instantiates an linked list item instance
        """
        if item:
            self._node_item = item
            self._next_node = None
        else:
            raise SingleLinkedListException("cannot insert empty item as linked list item")

    def get_item(self):
        """get_item() - returns the node item
        """
        return self._node_item

    def set_item(self, item=None):
        """set_item() -  returns the node item
        """
        if item:
            self._node_item = item
        else:
            raise SingleLinkedListException("cannot insert empty item as linked list item")

    def get_next(self):
        """get_next() - returns the next item
        """
        return self._next_node

    def set_next(self, next_node=None):
        """set_next() - sets the next item
        """
        self._next_node = next_node

    def __repr__(self):
        """__repr__() - returns the debugging information
        """
        return ('item : {}, next : {}').format(self._node_item, self._next_node)


class SingleLinkedList:
    """Single LinkedList implementation
    """
    def __init__(self):
        """intantiates the singe linked list instance
        """
        self._head_node = None
        self._tail_node = None
        self._current_iter_node = None

    def add(self, item=None):
        """add() - adds an item to the linked list
        """
        try:
            node = Node(item)
            if self._head_node:
                self._tail_node.set_next(node)
                self._tail_node = node
            else:
                self._head_node = node
                self._tail_node = node
        except:
            raise

    def insert(self, index=None, item=None):
        """isert() - inserts the item at the specific index
        """
        total_nodes = self.size()
        if (index >= 0) and (index < total_nodes):
            index_counter = 0
            inserted = False
            prev_node = None
            current_node = self._head_node
            while index_counter < total_nodes and not inserted:
                if index_counter == index:
                    node = Node(item)
                    node.set_next(current_node)
                    if prev_node:
                        prev_node.set_next(node)
                    else:
                        self._head_node = node
                    inserted = True
                index_counter += 1
                prev_node = current_node
                current_node = current_node.get_next() 
        elif index == -1:
            try:
                self.add(item=item)
            except:
                raise
        else:
            raise SingleLinkedListException('insert operation not supported on the supplied index')

    def delete_index(self, index=None):
        """delete_index() - deletes item based in index value
        """
        total_nodes = self.size()
        if (index >= 0) and (index < total_nodes):
            index_counter = 0
            deleted = False
            prev_node = None
            current_node = self._head_node
            while index_counter < total_nodes and not deleted:
                if index_counter == index:
                    if prev_node:
                        prev_node.set_next(current_node.get_next())
                        if not current_node.get_next():
                            self._tail_node = prev_node
                    else:
                        self._head_node = current_node.get_next()
                    deleted = True
                index_counter += 1
                prev_node = current_node
                current_node = current_node.get_next()
        else:
            raise SingleLinkedListException('Operation not permitted, either list is empty or index not valid')

    def delete_item(self, item=None):
        """delete_item() - deletes item based on the item value
        """
        current_node = self._head_node
        prev_node = None
        deleted = False
        while current_node and not deleted:
            if current_node.get_item() == item:
                if prev_node:
                    prev_node.set_next(current_node.get_next())
                    if not current_node.get_next():
                        self._tail_node = prev_node
                else: 
                    self._head_node = current_node.get_next()
                deleted = True
            prev_node = current_node
            current_node = current_node.get_next()

    def reverse_list(self):
        """reverse_list() - reverses the linked list
        """
        if not self._head_node or not self._head_node.get_next():
            return

        current_node = self._head_node
        next_node = current_node.get_next()
        prev_node = None

        while current_node:
            current_node.set_next(prev_node)
            prev_node = current_node
            current_node = next_node
            if next_node:
                next_node = next_node.get_next()
        self._head_node, self._tail_node = self._tail_node, self._head_node

    def is_empty(self):
        """is_empty() - returns True, if list is empty, else False
        """
        return self._head_node == None

    def size(self):
        """size() - returns size of the linked list
        """
        return len(list(self))
        
    def __iter__(self):
        """__iter() - iter method, making it iterable
        """
        self._current_iter_node = self._head_node
        return self

    def next(self):
        """next() - returns next element from the list
        """
        if self._current_iter_node:
            item = self._current_iter_node.get_item()
            self._current_iter_node = self._current_iter_node.get_next()
            return item
        else:
            raise StopIteration 

    def print_list(self):
        """print_list() - prints the linked list
        """
        for node in self:
            print str(node) + " -> ",
        print None


if __name__ == '__main__':
    li = SingleLinkedList()
    li.add(1)
    li.add(2)
    li.add(2)
    li.add(2)
    li.add(2)
    li.add(2)
    li.add(3)
    li.print_list()
    li.delete_item(2)
    li.add(4)
    li.print_list()
    

