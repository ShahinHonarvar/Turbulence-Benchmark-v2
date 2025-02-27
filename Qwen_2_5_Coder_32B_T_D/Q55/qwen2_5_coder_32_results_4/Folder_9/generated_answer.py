from collections import deque

def lists_with_product_equal_n(lst):
    n = -36
    result = []
    lst = deque(lst)
    size = len(lst)
    for start in range(size):
        product = 1
        sublist = []
        for i in range(size):
            product *= lst[(start + i) % size]
            sublist.append(lst[(start + i) % size])
            if product == n:
                result.append(sublist[:])
            if product == 0:
                break
    return result