"""Write a method that detach a node from the tree
Given a basic BST structure (included), add a _detach_node() method to it, to search for values in the tree. 
The basic definition of the method is already included. The method accepts the node to be deleted as parameter and 
returns nothing.

The method should check on parent and possible children to change the connections and be sure that the tree remains 
functional after safely detaching the node from the tree. If the node to detach has two children, the method should 
raise a ValueError (it is not possible to just detach a node with two children from a BST). The method should also 
take into account when the node to detach is the root node.

Notice that the Node object, when printed, prints some odd code. This is done on purpose to help checking on the 
exercises."""

class Node():
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent = parent_node
        self._left_child = left_child
        self._right_child = right_child

    def __repr__(self):
        left = self._left_child if self._left_child is not None else ''
        right = self._right_child if self._right_child is not None else ''
        return f'{self.data}<{left}><{right}>#'


class Tree():
    def __init__(self):
        self._root_node = None

    def __repr__(self):
        return f'<Tree: {self._root_node}>'

    def insert(self, data):
        current_node = self._root_node
        parent_node = None
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child

        new_node = Node(data, parent_node=parent_node)
        if parent_node is None:
            if self._root_node is None:
                self._root_node = new_node
            else:
                raise(ValueError)
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node

    def _find(self, data):
        current = self._root_node
        while current:
            if current.data == data:
                return current
            elif current.data > data:
                current = current._left_child
            else:
                current = current._right_child
        return None        

    def _detach_node(self, node):
        if node._left_child and node._right_child:
            raise ValueError

        child = node._left_child if node._left_child else node._right_child
        parent = node._parent

        if parent is None:
            self._root_node = child
            if child:
                child._parent = None
        else:
            if parent._left_child == node:
                parent._left_child = child
            else:
                parent._right_child = child
            if child:
                child._parent = parent

        node._parent = None
        node._left_child = None
        node._right_child = None
