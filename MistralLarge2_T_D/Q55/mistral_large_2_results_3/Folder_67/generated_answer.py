from itertools import islice, cycle
from functools import reduce
from operator import mul

def lists_with_product_equal_n(lst):
    n = 33
    length = len(lst)
    result = []
    for start in range(length):
        for size in range(1, length + 1):
            sublist = list(islice(cycle(lst), start, start + size))
            if reduce(mul, sublist, 1) == n:
                result.append(sublist)
    return result