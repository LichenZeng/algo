
class ArrayStack:
    def __init__(self, capacity) -> None:
        self._item = []
        self._capacity = capacity
        self._count = 0

    def push(self, value):
        if self._count >= self._capacity:
            return False
        # self._item[self._count] = value
        # self._item.insert(self._count, value)
        self._item.append(value)
        self._count += 1
        return True

    def pop(self):
        if self._count <= 0:
            return None
        self._count -= 1
        # return self._item[self._count]
        return self._item.pop()

    def print(self):
        print("item, cap, count: ", self._item, self._capacity, self._count)


if __name__ == '__main__':
    arrayStack = ArrayStack(5)
    arrayStack.print()

    arrayStack.push(10)
    arrayStack.push(20)
    arrayStack.push(30)
    arrayStack.print()

    print(arrayStack.pop())
    print(arrayStack.pop())
    print(arrayStack.pop())
    print(arrayStack.pop())
