
class ArrayQueue:
    def __init__(self, capacity) -> None:
        self._item = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue_01(self, value):
        if self._tail >= self._capacity:
            return False
        self._item.insert(self._tail, value)
        self._tail += 1
        return True

    def enqueue(self, value):
        if self._tail >= self._capacity and self._head == 0:
            return False
        else:
            i = self._head
            while i < self._tail:
                self._item[i - self._head] = self._item[i]
                i += 1
            self._tail -= self._head
            self._head = 0
        self._item.insert(self._tail, value)
        self._tail += 1
        return True

    def dequeue(self):
        if self._head == self._tail:
            return None
        value = self._item[self._head]
        self._head += 1
        return value

    def print(self):
        print("item, cap, head, tail: ", self._item[self._head:self._tail],
              self._capacity, self._head, self._tail)


class ArrayCircleQueue:
    def __init__(self, capacity) -> None:
        self._item = [None] * capacity
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, value):
        if (self._tail + 1) % self._capacity == self._head:
            return False
        self._item[self._tail] = value
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self):
        if self._head == self._tail:
            return None
        value = self._item[self._head]
        self._head = (self._head + 1) % self._capacity
        return value

    def print(self):
        if self._tail >= self._head:
            print("item, cap, head, tail: ", self._item[self._head:self._tail],
                  self._capacity, self._head, self._tail)
        else:
            print("item, cap, head, tail: ", self._item[self._head:] + self._item[0:self._tail],
                  self._capacity, self._head, self._tail)


if __name__ == '__main__':
    queue = ArrayQueue(6)
    queue.print()

    for i in range(5):
        queue.enqueue(i)
    queue.print()

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    queue.print()

    queue.enqueue(111)
    queue.print()
    queue.enqueue(222)
    queue.enqueue(333)
    queue.print()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.print()

    for i in range(6):
        print(queue.dequeue())
    queue.print()

    print("====== CircleQueue ======")
    circleQueue = ArrayCircleQueue(6)
    circleQueue.print()

    for i in range(5):
        circleQueue.enqueue(i)
    circleQueue.print()

    print(circleQueue.dequeue())
    print(circleQueue.dequeue())
    print(circleQueue.dequeue())
    circleQueue.print()

    circleQueue.enqueue(111)
    circleQueue.print()
    circleQueue.enqueue(222)
    circleQueue.enqueue(333)
    circleQueue.print()
    circleQueue.dequeue()
    circleQueue.dequeue()
    circleQueue.dequeue()
    circleQueue.print()

    for i in range(6):
        print(circleQueue.dequeue())
    circleQueue.print()
