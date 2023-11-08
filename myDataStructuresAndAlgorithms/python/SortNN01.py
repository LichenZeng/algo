
class SortNN:
    def __init__(self) -> None:
        self._item = []

    def sort_with_bubble(self, list):
        self._item = list
        if list is None or len(list) == 1:
            return
        for i in range(len(list) - 1):
            for j in range(len(list) - i - 1):
                if list[j] > list[j+1]:
                    tmp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = tmp

    def sort_with_insert(self, list):
        self._item = list
        if list is None or len(list) == 1:
            return
        for i in range(1, len(list)):
            value = list[i]
            j = i - 1
            while j >= 0:
                if list[j] > value:
                    list[j+1] = list[j]
                    j -= 1
                else:
                    break
            list[j + 1] = value

    def sort_with_select(self, list):
        self._item = list
        if list is None or len(list) == 1:
            return
        for i in range(len(list) - 1):
            min = list[i]
            k = i
            for j in range(i, len(list)):
                if list[j] < min:
                    min = list[j]
                    k = j
            list[k] = list[i]
            list[i] = min

    def print(self):
        print(self._item)


if __name__ == '__main__':
    # list01 = [1, 2, 3, 4, 5]
    # list01 = [3, 2, 1, 5, 4]
    list01 = [3, 1, 2, 5, 4]
    sort = SortNN()
    # sort.sort_with_bubble(list01)
    # sort.sort_with_insert(list01)
    sort.sort_with_select(list01)
    print(list01)


"""
    def sort_with_insert(self, list):
        self._item = list
        if list is None or len(list) == 1:
            return
        for i in range(1, len(list)):
            value = list[i]
            # j = i - 1
            # while j >= 0:
            #     if list[j] > value:
            #         list[j+1] = list[j]
            #         j -= 1
            #     else:
            #         break
            # list[j + 1] = value
            for j in range(i-1, -1, -1):
                print(j)
                if list[j] > value:
                    list[j+1] = list[j]
                    list[j] = value
                    j -= 1   # 需要考虑正常退出循环的情况
                else:
                    break
            print(j+1)
            list[j+1] = value
            print(list)

"""
