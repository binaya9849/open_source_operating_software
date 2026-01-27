"""
Implement insert method for a Doubly linked list
You will have to implement the insert method, that inserts a new element/node in the list at the position given as a parameter.

The insert method will accept an index position where to insert a new node. The value of the node is the second parameter that have to be provided to the method. The method does not return anything, but it will raise a ValueError if the index is out of bounds.

The process is quite straight. Locate the nodes that will be before and after the new node, and update the necessary pointers. If the header pointer is affected, it should be updated. And the same happens with tail pointer.

For example:

Test	Result
mylist = DoublyLinkedList()
for i in range(10, 51, 10):
    mylist.append(i)
mylist.insert(0, 5)
print(mylist)
<DoublyLinkedList (6 elements): [5, 10, 20, 30, 40, 50]>
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



mylist = DoublyLinkedList()

for i in range(10, 51, 10):
    mylist.append(i)
print("After append:", mylist)

mylist.insert(0, 5)
print("After insert at index 0:", mylist)

mylist.insert(3, 25)
print("After insert at index 3:", mylist)

mylist.insert(mylist._size, 60) 
print("After insert at the end:", mylist)

print("Program finished")

