from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self, val) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insertHead(self, val) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def get(self, index):
        if not self.head:
            return -1

        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next

        return -1  # Index out of bounds

    def remove(self, index) -> bool:
        curr = self.head
        prev = None

        if not curr:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        for i in range(index):
            prev = curr
            curr = curr.next
            if not curr:
                return False

        prev.next = curr.next
        return True

    def traverse(self) -> List[int]:
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr


LL = LinkedList()
LL.insertTail(2)
print(LL.traverse())
LL.insertTail(5)
print(LL.traverse())
LL.insertHead(12)
print(LL.traverse())
LL.insertHead(-7)
print(LL.traverse())
LL.insertTail(14)
print(LL.traverse())
print(LL.get(0))
print(LL.get(2))
print(LL.get(4))
print('Removing element at position: 1')
print(LL.remove(1) is True)
print(LL.traverse())
print('Removing element at position: 0')
print(LL.remove(0) is True)
print(LL.traverse())
print('Removing element at position: 2')
print(LL.remove(2) is True)
print(LL.traverse())
print('Removing element at position: 3')
print(LL.remove(3) is False)
print(LL.traverse())
print('Removing element at position: 0')
print(LL.remove(0) is True)
print(LL.traverse())
print('Removing element at position: 1')
print(LL.remove(1) is False)
print(LL.traverse())
