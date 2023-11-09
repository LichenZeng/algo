import random


class SortNLogN:
    def __init__(self) -> None:
        self._item = []

    def sort_with_merge(self, list):
        self._item = list
        if list is None or len(list) == 1:
            return
        self.__merge_sort(list, 0, len(list) - 1)

    def __merge_sort(self, list, start, end):
        if start == end:
            return
        mid = start + (end - start)//2
        self.__merge_sort(list, start, mid)
        self.__merge_sort(list, mid+1, end)
        self.__merge(list, start, mid, end)

    def __merge(self, list, start, mid, end):
        # print("debug list", list[start:mid+1], list[mid+1:end+1])
        tmp = [0] * (end - start + 1)
        i = start
        j = mid + 1
        k = 0
        while i <= mid and j <= end:
            if list[i] < list[j]:
                tmp[k] = list[i]
                i += 1
            else:
                tmp[k] = list[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = list[i]
            i += 1
            k += 1
        while j <= end:
            tmp[k] = list[j]
            j += 1
            k += 1
        for i in range(start, end + 1):
            list[i] = tmp[i - start]
        # print("debug tmp", tmp)
        # print("debug list", list[start:end+1])

    def sort_with_quick(self, list):
        self._item = list
        if list is None or len(list) == 1:
            return
        self.__quick_sort(list, 0, len(list) - 1)

    def __quick_sort(self, list, start, end):
        if start >= end:
            return
        pivot = self.__partition(list, start, end)
        self.__quick_sort(list, start, pivot - 1)
        self.__quick_sort(list, pivot + 1, end)

    def __partition(self, list, start, end):
        print("debug list1: ", list[start:end+1])
        pivot = end
        mid = start + (end - start)//2
        if list[start] > list[pivot] and list[mid] > list[pivot]:
            if list[start] > list[mid]:
                pivot = mid
            else:
                pivot = start
        if list[start] < list[pivot] and list[mid] < list[pivot]:
            if list[start] > list[mid]:
                pivot = start
            else:
                pivot = mid
        print("debug pivot1: ", pivot)
        if pivot != end:
            list[pivot], list[end] = list[end], list[pivot]
            pivot = end
        i = start
        for j in range(start, end):
            if list[j] < list[pivot]:
                list[i], list[j] = list[j], list[i]
                i += 1
        list[i], list[pivot] = list[pivot], list[i]
        pivot = i
        print("debug list2: ", list[start:end+1])
        print("debug pivot2: ", pivot)
        return pivot


if __name__ == '__main__':
    # list1 = [1, 2, 3, 4, 5]
    # list1 = [5, 4, 3, 2, 1]
    list1 = [5, 3, 1, 2, 4]
    for i in range(100):
        list1.append(random.randrange(0, 100))

    sort = SortNLogN()
    print(list1)
    # sort.sort_with_merge(list1)
    sort.sort_with_quick(list1)
    print(list1)
