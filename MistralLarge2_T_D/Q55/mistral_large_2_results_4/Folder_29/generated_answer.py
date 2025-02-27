from collections import deque
from itertools import islice

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = list(islice(deque(circular_list), i, i + j))
            if len(sublist) == j and product(sublist) == 15:
                result.append(sublist)
    return result

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod