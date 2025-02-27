from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = deque(lst)
    result = []
    for _ in range(n):
        product = 1
        for j in range(n):
            product *= lst[j]
            if product == -89:
                result.append(list((lst[i % n] for i in range(j + 1))))
        lst.appendleft(lst.pop())
    return result