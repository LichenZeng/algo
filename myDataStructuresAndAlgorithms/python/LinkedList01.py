class Node:
    def __init__(self, item) -> None:
        self._item = item
        self._next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self._head = None
        self._tail = None

    def append(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        return True

    def insert(self, index, item):
        node = Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
        elif index <= 0:
            node._next = self._head
            self._head = node
        else:
            cur = self._head
            pre = self._head
            count = 0
            while (cur._next is not None) and (count < index):
                count += 1
                pre = cur
                cur = cur._next
            if cur._next is None:
                self._tail._next = node
                self._tail = node
            else:
                node._next = pre._next
                pre._next = node
        return True

    def remove(self, index):
        if self._head is None:
            self._head = None
            self._tail = None
        elif index <= 0:
            cur = self._head
            self._head = cur._next
            cur._next = None
        else:
            cur = self._head
            pre = self._head
            count = 0
            while (cur._next is not None) and (count < index):
                count += 1
                pre = cur
                cur = cur._next
            if cur._next is None:
                self._tail = pre
                pre._next = None
            else:
                pre._next = cur._next
                cur._next = None
        return True

    def reverse(self):
        if self._head is None or self._head._next is None:
            return
        pre = self._head
        cur = self._head._next
        pre._next = None
        self._tail = pre

        # reverse node(addr&value)
        while cur is not None:
            self._head = cur
            cur = cur._next
            self._head._next = pre
            pre = self._head

    def print(self):
        print("Linked list node:", end=" ")
        cur = self._head
        while cur is not None:
            print(cur._item, end=" ")
            cur = cur._next
        print()


if __name__ == '__main__':
    linkedList = SingleLinkedList()
    for i in range(10):
        linkedList.insert(0, i)
    linkedList.print()

    linkedList.insert(0, 111)
    linkedList.insert(5, 222)
    linkedList.insert(30, 333)
    linkedList.print()

    linkedList.remove(30)
    linkedList.remove(5)
    linkedList.remove(0)
    linkedList.print()

    linkedList.reverse()
    linkedList.print()

    for i in range(10, 20):
        linkedList.append(i)
    linkedList.print()


"""  code snippet backup

    def add(self, item):
        node = Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            node._next = self._head
            self._head = node
        return True

    def append(self, item) -> int:
        # if not isinstance(item, int):
        #     raise TypeError("item must be integers")
        node = Node(item)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node
        return True

    def reverse(self):
        if self._head is None or self._head._next is None:
            return
        pre = self._head
        cur = self._head._next
        pre._next = None
        self._tail = pre

        # reverse node(addr&value)
        while cur is not None:
            self._head = cur
            cur = cur._next
            self._head._next = pre
            pre = self._head

        # Just reverse value, use new node
        # while cur is not None:
        #     self.insert(0, cur._item)
        #     cur = cur._next

        
    def fake_reverse(self):
        cur = self._head
        item = []
        while cur._next is not None:
            item.append(cur._item)
            cur = cur._next
        print(item)
        item.reverse()
        print(item)

"""
