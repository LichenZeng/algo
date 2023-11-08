import time

haveSolved = {}


def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return func(n - 1) + func(n - 2)


def func_with_map(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n not in haveSolved.keys():
        haveSolved[n] = func(n - 1) + func(n - 2)
    return haveSolved[n]


stairs = 35

t1 = time.time()
climb_num = func(stairs)
print("Climb stairs: ", climb_num)
print(time.time() - t1)

t2 = time.time()
climb_num = func_with_map(stairs)
print("Climb stairs with map: ", climb_num)
print(time.time() - t2)


"""
如果计算本身不是太耗时，添加了map 的方法，其耗时反而会高点
Climb stairs:  14930352
2.5194082260131836
Climb stairs with map:  14930352
2.5229172706604004
"""
