""" 
Implement remove method for a Singly linked list with tail
You will have to implement a more general remove method that can remove list's nodes from any position. To help in this task an insert method is also provided that works as an example on how this method has to be implemented.

The remove method will accept an index position of a node to be removed and it will return the value of the node being removed. If the index is out of bounds, ValueError has to be raised. The method should update head and tail if necessary, and the size of the list.

Answer:(penalty regime: 0 %)
"""
class ListNode():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<ListNode: {self.data}>'


class SinglyLinkedList():
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __repr__(self):
        current_node = self._head
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.next
        plural = '' if self._size == 1 else 's'
        return f'<SinglyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        new_node = ListNode(value)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def pop(self):
        if not self._size:
            return None

        if self._size == 1:
            value = self._head.data
            del self._head
            self._head = self._tail = None
            self._size = 0
            return value

        previous_node = self._head
        for _ in range(self._size - 2):
            previous_node = previous_node.next

        value = self._tail.data
        del self._tail
        self._tail = previous_node
        self._tail.next = None
        self._size -= 1
        return value

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        next_node = self._head

        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        new_node = ListNode(value, next_node)

        if previous_node is None:
            self._head = new_node
        else:
            previous_node.next = new_node

        if previous_node == self._tail:
            self._tail = new_node

        self._size += 1

    def remove(self, index):
        # Same structure as insert (Exercise 1)
        if index < 0 or index >= self._size:
            raise(ValueError('Index out of bounds'))

        previous_node = None
        next_node = self._head

        for _ in range(index):
            previous_node = next_node
            next_node = next_node.next

        value = next_node.data

        if previous_node is None:
            self._head = next_node.next
        else:
            previous_node.next = next_node.next

        if next_node == self._tail:
            self._tail = previous_node

        del next_node
        self._size -= 1
        return value

if __name__ == "__main__":
    mylist = SinglyLinkedList()

    for i in range(1, 6):
        mylist.append(i * 10)

    print("Before remove:", mylist)

    val = mylist.remove(2)
    print("Removed value:", val)

    print("After remove:", mylist)
