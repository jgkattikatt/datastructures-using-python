#TREE IMPLEMENTATION IN PYTHON
#jgkattikatt@gmail.com


class TreeException(Exception):
    """tree exception class
    """
    pass


class Node:
    """node implementation
    """
    def __init__(self, item=None):
        """instantiates a node item
        """
        if item:
            self._item = item
        else:
            raise TreeException("Node item value cannot be empty")
        self._left_node = None
        self._right_node = None

    def get_item(self):
        """get_item() - returns the node item value
           args - None
           return - item
        """
        return self._item

    def set_item(self, item=None):
        """set_item() - 
        """
        if item:
            self._item = item
        else:
            raise TreeException("Node item value cannot be empty")

    def get_left_node(self):
        """get_left_node() - 
        """
        return self._left_node
        
    def set_left_node(self, node=None):
        """set_left_node() - 
        """
        self._left_node = node

    def get_right_node(self):
        """get_right_node() - 
        """
        return self._right_node

    def set_right_node(self, node):
        """set_right_node() -
        """
        self._right_node = node
        
        
class BinaryTree:
    """binary tree implementation
       interfaces : insert, search, traversal
    """
    
    def __init__(self):
        """intantiate a binary tree instance
        """
        self._root_node = None

    def insert(self, item=None):
        """insert() - insert an item to the tree
        """
        try:
            print 'processing - {}'.format(item) 
            node = Node(item)            
        except:
            raise
        else:
            if self._root_node:
                self._traverse_and_insert_item(self._root_node, node)
            else:
                self._root_node = node
               

    def traverse_tree(self, traverse_type):
        """
        """
        if traverse_type in ["preorder"]:
            self._preorder_traversal(self._root_node)
        elif traverse_type == "inorder":
            self._inorder_traversal(self._root_node)
        elif traverse_type == "postorder":
            self._postorder_traversal(self._root_node)
        else:
            print "{} - traversal type not supported".format(traverse_type)
        print "\n"

    def delete_node(self):
        """
        """
        pass

    def search(self):
        """
        """
        pass

    def _traverse_and_insert_item(self, root_node=None, node=None):
        """_traverse_and_insert_item() - traverse and insert element to the tree
        """
        keep_traversing = True

        while keep_traversing:            
            if node.get_item() >= root_node.get_item():                
                if root_node.get_right_node():
                    root_node = root_node.get_right_node()
                else:
                    root_node.set_right_node(node)
                    keep_traversing = False                    
            else:                
                if root_node.get_left_node():
                    root_node = root_node.get_left_node()
                else:
                    root_node.set_left_node(node)
                    keep_traversing = False


    def _preorder_traversal(self, node):
        """_preorder_traversal - traverse tree in preorder style (root, left, right)
        """
        if not node:            
            return
        
        print node.get_item(),
        self._preorder_traversal(node.get_left_node())
        self._preorder_traversal(node.get_right_node())

    def _inorder_traversal(self, node):
        """_inorder_traversal - traverse tree in preorder style (left, root, right)
        """
        if not node:            
            return

        self._preorder_traversal(node.get_left_node())
        print node.get_item(),
        self._preorder_traversal(node.get_right_node())

    def _postorder_traversal(self, node):
        """_postorder_traversal - traverse tree in preorder style (left, right, root)
        """
        if not node:            
            return

        self._preorder_traversal(node.get_left_node())
        self._preorder_traversal(node.get_right_node())
        print node.get_item(),
                   
                
if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(6)
    bt.insert(2)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(10)
    bt.traverse_tree("preorder")
    bt.traverse_tree("inorder")
    bt.traverse_tree("postorder")
