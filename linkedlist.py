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
        """
        """
        return self._node_item

    def set_item(self, item=None):
        """
        """
        if item:
            self._node_item = item
        else:
            raise SingleLinkedListException("cannot insert empty item as linked list item")

    def get_next(self):
        """
        """
        return self._next_node

    def set_next(self, next_node=None):
        """
        """
        self._next_node = next_node

    def __repr__(self):
        """
        """
        return ('item : {}, next : {}').format(self._node_item, self._next_node)


class SingleLinkedList:
    """Single LinkedList implementation
    """
    def __init__(self):
        """
        """
        self._head_node = None
        self._tail_node = None
        self._current_iter_node = None

    def add(self, item=None):
        """
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
        """
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

    def delete(self, index=None):
        """
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
                    else:
                        self._head_node = current_node.get_next()
                    deleted = True
                index_counter += 1
                prev_node = current_node
                current_node = current_node.get_next()
        else:
            raise SingleLinkedListException('Operation not permitted, either list is empty or index not valid')

    def is_empty(self):
        """
        """
        return self._head_node == None

    def size(self):
        """
        """
        return len(list(self))
        
    def __iter__(self):
        """
        """
        self._current_iter_node = self._head_node
        return self

    def next(self):
        """
        """
        if self._current_iter_node:
            item = self._current_iter_node.get_item()
            self._current_iter_node = self._current_iter_node.get_next()
            return item
        else:
            raise StopIteration 

    def print_list(self):
        """
        """
        for node in self:
            print str(node) + " -> ",
        print None


if __name__ == '__main__':
    li = SingleLinkedList()
    li.add(1)
    li.add(2)
    li.add(3)
    li.print_list()
    print li.size()
    li.insert(-1, 4)
    li.print_list()
    print li.size()
    li.delete(1)
    li.print_list()
    

