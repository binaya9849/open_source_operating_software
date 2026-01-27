"""
Implementing a pop method for a Singly linked list
Given the base code we have seen until now and that is also provided, implement a pop method

The pop method will remove the last element from the list and return the data it contains. If the list is empty it should return None

This is a little bit trickier than the insert, as the method should take into account different cases: List is empty, list has only one node and then the rest of cases. The method should also locate the second to last node, to change its "next" pointer.

To actually remove a variable (like a node), remember you can use the del statement:

del(variable)

For example:

Test	Result
list = SinglyLinkedList()
for i in 'abc':
    list.append(i)
val = list.pop()
print(val, list)
c <SinglyLinkedList: [a, b]>

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def pop(self):
        if self.head is None:
            return None

        if self.head.next is None:
            value = self.head.data
            self.head = None
            return value

        current = self.head
        while current.next.next is not None:
            current = current.next

        value = current.next.data
        current.next = None
        return value

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return "<SinglyLinkedList: [" + ", ".join(values) + "]>"



print("Program started")

my_list = SinglyLinkedList()

print("Appending values: a, b, c")
for ch in "abc":
    my_list.append(ch)

print("Current list:", my_list)

popped_value = my_list.pop()
print("Popped value:", popped_value)

print("List after pop:", my_list)

print("Program finished")
