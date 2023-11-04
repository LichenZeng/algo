from LinkedList01 import Node


def reverse_list(list):
    if list is None or list._next is None:
        return
    pre = list
    cur = list._next
    pre._next = None

    # reverse node(addr&value)
    while cur is not None:
        list = cur
        cur = cur._next
        list._next = pre
        pre = list
    return list


def is_circle_in_list(list):
    if list is None or list._next is None:
        return False
    fast = list
    slow = list

    while slow is not None and fast is not None:
        slow = slow._next
        fast = fast._next._next
        if slow is fast:
            return True
    return False


def merge_list(list1, list2):
    if list1 is None or list2 is None:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

    head = None
    cur1 = list1
    cur2 = list2
    if cur1._item < cur2._item:
        head = cur1
        cur1 = cur1._next
    else:
        head = cur2
        cur2 = cur2._next
    head._next = None
    tail = cur = head

    if cur1 is None:
        cur._next = cur2
        return head
    elif cur2 is None:
        cur._next = cur1
        return head

    while cur1._next is not None and cur2._next is not None:
        if cur1._item <= cur2._item:
            cur = cur1
            cur1 = cur1._next
        else:
            cur = cur2
            cur2 = cur2._next
        cur._next = None
        tail._next = cur
        tail = cur

    if cur1._next is None:
        cur._next = cur2
    else:
        cur._next = cur1

    return head


def remove_k_node_to_last(list, k):
    if list is None:
        return None

    cur = list
    count = 0
    while cur._next is not None:
        cur = cur._next
        count += 1
    if count < k:
        raise IndexError("the k-th node is not exist!")

    cur = list
    if count == k:
        list = list._next
        cur._next = None
    else:
        loop = count - k - 1
        while loop > 0:
            cur = cur._next
            loop -= 1
        tmp = cur._next
        cur._next = cur._next._next
        tmp._next = None

    return list


def get_mid_node(list):
    if list is None or list._next is Node:
        return list

    cur = list
    count = 0
    while cur._next is not None:
        cur = cur._next
        count += 1

    mid = count / 2
    cur = list
    while mid > 0:
        cur = cur._next
        mid -= 1

    return cur


def print_list(list):
    cur = list
    while cur is not None:
        print(cur, cur._item)
        cur = cur._next
    print()


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    print("=== get middle node in list ===")
    head = node1
    node1._next = node3
    node3._next = node4
    node4._next = node6
    node6._next = node7
    node7._next = None
    print_list(head)
    node = get_mid_node(head)
    if node is not None:
        print(node, node._item)

    # print("=== remove k-th node to last ===")
    # head = node1
    # node1._next = node2
    # node2._next = node3
    # node3._next = node4
    # node4._next = None
    # print_list(head)
    # new = remove_k_node_to_last(head, 3)
    # print_list(new)

    # print("=== reverse list ===")
    # head = node1
    # node1._next = node2
    # node2._next = node3
    # node3._next = node4
    # node4._next = None

    # print("Before reverse:")
    # print_list(head)
    # head = reverse_list(head)
    # print("After reverse:")
    # print_list(head)

    # print("=== is circle in list ===")
    # head = node1
    # node1._next = node2
    # node2._next = node3
    # node3._next = node4
    # node4._next = node2
    # # print_list(head)
    # print("have circle: ", is_circle_in_list(head))

    # print("\n=== merge list ===")
    # head1 = node1
    # node1._next = node3
    # node3._next = node4
    # node4._next = node6
    # node6._next = node7
    # node7._next = None

    # head2 = node2
    # node2._next = node5
    # node5._next = node8
    # node8._next = node9
    # node9._next = None
    # print_list(head1)
    # print_list(head2)
    # head = merge_list(head2, head1)
    # print_list(head)
    # # head = merge_list(node1, node7)
    # # print_list(head)


"""
有问题的逻辑
def merge_list(list1, list2):
    if list1 is None or list2 is None:
        if list1 is None: 
            return list2
        elif list2 is None:
            return list1 

    head = None
    if list1._item < list2._item:
        head = list1
    else:
        head = list2

    cur1 = list1
    cur2 = list2
    while cur1._next is not None and cur2._next is not None:
        if cur1._item <= cur2._item:
            if cur1._next._item > cur2._item:
                tmp1 = cur1._next
                tmp2 = cur2._next
                cur2._next = cur1._next
                cur1._next = cur2
                cur1 = tmp1
                cur2 = tmp2
            else:
                cur1 = cur1._next
        else:
            if cur2._next._item > cur1._item:
                tmp1 = cur1._next
                tmp2 = cur2._next
                cur1._next = cur2._next
                cur2._next = cur1
                cur1 = tmp1
                cur2 = tmp2
            else:
                cur2 = cur2._next

    if cur1._next is None:
        cur1._next = cur2
    else:
        cur2._next = cur1

    return head

"""
