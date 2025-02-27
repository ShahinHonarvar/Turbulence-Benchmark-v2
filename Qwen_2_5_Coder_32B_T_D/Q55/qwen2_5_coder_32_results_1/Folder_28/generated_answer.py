from collections import deque

def lists_with_product_equal_n(lst):
    n = 85
    d = deque(lst)
    result = []
    l = len(lst)
    for start in range(l):
        product = 1
        current_list = []
        for i in range(l):
            product *= d[i]
            current_list.append(d[i])
            if product == n:
                result.append(current_list[:])
            if product > n:
                break
        d.rotate(-1)
    return result