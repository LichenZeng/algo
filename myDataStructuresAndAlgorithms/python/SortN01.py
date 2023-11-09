import random


class SortN:
    def __init__(self) -> None:
        self._item = []

    def sort_with_count(self, list):
        self._item = list
        if list is None or len(list) == 1:
            return
        max = list[0]
        for i in range(len(list)):
            if list[i] > max:
                max = list[i]
        # print("debug max: ", max)
        tmp = [0] * (max + 1)
        for i in range(len(list)):
            tmp[list[i]] += 1
        # print("debug tmp: ", tmp)

        for j in range(1, len(tmp)):
            tmp[j] += tmp[j - 1]
        # print("debug tmp count: ", tmp)

        tlist = [None] * len(list)
        for i in range(len(list)):
            tlist[tmp[list[i]] - 1] = list[i]
            tmp[list[i]] -= 1
        # print("debug tlist: ", tlist)
        for i in range(len(list)):
            list[i] = tlist[i]


if __name__ == '__main__':
    list1 = [5, 1, 3, 4, 3]
    for i in range(100):
        list1.append(random.randrange(0, 100))
    print(list1)

    sort = SortN()
    sort.sort_with_count(list1)
    print(list1)
