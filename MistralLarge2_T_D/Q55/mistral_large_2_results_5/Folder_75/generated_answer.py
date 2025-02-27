from collections import deque
from itertools import islice

def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for x in lst:
            result *= x
        return result
    n = len(circular_list)
    result = []
    circular_list = deque(circular_list)
    for i in range(n):
        for length in range(1, n + 1):
            sublist = list(islice(circular_list, length))
            if product(sublist) == 13:
                result.append(sublist)
        circular_list.rotate(-1)
    return result