""" 
Implement remove method for a Doubly linked list
You will have to implement the remove method, that removes a element/node from the list at the position given as a parameter.

The remove method will accept an index position from where to remove node from the list. The method has to return the value of the node being removed or None if the list is empty. The method will raise a ValueError if the index is out of bounds.

The process is quite straight. Locate the nodes that before and after the node to be removed, and update the necessary pointers. If the header pointer is affected, it should be updated. And the same happens with tail pointer.


For example:

Test	Result
mylist = DoublyLinkedList()
for i in range(10, 51, 10):
    mylist.append(i)
val = mylist.remove(2)
print(val, mylist)
30 <DoublyLinkedList (4 elements): [10, 20, 40, 50]>
Answer:(penalty regime: 0 %)
"""

class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'

class DoublyLinkedList:
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
        return f'<DoublyLinkedList ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def __len__(self):
        return self._size

    def append(self, value):
        new_node = ListNode(value, next=None, prev=self._tail)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise ValueError('Index out of bounds')
        if index == self._size:
            self.append(value)
            return
        next_node = self._head
        for _ in range(index):
            next_node = next_node.next
        previous_node = next_node.prev
        new_node = ListNode(value, next=next_node, prev=previous_node)
        if previous_node:
            previous_node.next = new_node
        else:
            self._head = new_node
        next_node.prev = new_node
        self._size += 1

    def remove(self, index):
        if index < 0 or index >= self._size:
            raise ValueError('Index out of bounds')
        current_node = self._head
        for _ in range(index):
            current_node = current_node.next
        previous_node = current_node.prev
        next_node = current_node.next
        if previous_node is None:
            self._head = next_node
        else:
            previous_node.next = next_node
        if next_node is None:
            self._tail = previous_node
        else:
            next_node.prev = previous_node
        value = current_node.data
        del current_node
        self._size -= 1
        return value

print("Program started")


mylist = DoublyLinkedList()
for i in range(10, 51, 10):
    mylist.append(i)
print("After append:", mylist)

mylist.insert(0, 5)
print("After insert at index 0:", mylist)

mylist.insert(3, 25)
print("After insert at index 3:", mylist)

mylist.insert(len(mylist), 60)
print("After insert at the end:", mylist)

val = mylist.remove(2)
print(f"Removed value at index 2: {val}, list now: {mylist}")

val = mylist.remove(0)
print(f"Removed value at index 0: {val}, list now: {mylist}")

val = mylist.remove(len(mylist) - 1)
print(f"Removed last value: {val}, list now: {mylist}")

print("Program finished")
