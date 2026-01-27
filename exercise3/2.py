"""
Implementing pop method for a Singly linked list with tail
Now the singly linked list has two pointers: a head pointer and a tail pointer. Some things are easier and faster this way. In this exercise you will implement again a pop method to the SinglyLinkedList class.

The pop methods will remove the last element/node from the list and return its value. Same as before, if the list is empty, it should return None. The method will update the head and tail properties accordingly.

To actually remove a variable (like a node), remember you can use the del statement:

del(variable)

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

        if not self._tail:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def pop(self):
        # Case 1: empty list
        if self._head is None:
            return None

        # Case 2: only one element
        if self._head == self._tail:
            value = self._head.data
            del self._head
            self._head = self._tail = None
            self._size = 0
            return value

        # Case 3: more than one element
        current = self._head
        while current.next != self._tail:
            current = current.next

        value = self._tail.data
        del self._tail
        self._tail = current
        self._tail.next = None
        self._size -= 1
        return value


print("Program started")

lst = SinglyLinkedList()
for ch in "abc":
    lst.append(ch)

print("List before pop:", lst)

popped = lst.pop()
print("Popped value:", popped)

print("List after pop:", lst)

print("List length:", len(lst))

print("Program finished")
