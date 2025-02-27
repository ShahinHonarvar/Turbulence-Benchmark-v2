from collections import deque

def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = deque(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[j]
            if product == 3:
                result.append(list(lst[:j + 1]))
            elif product > 3:
                break
        lst.append(lst.popleft())
    return result