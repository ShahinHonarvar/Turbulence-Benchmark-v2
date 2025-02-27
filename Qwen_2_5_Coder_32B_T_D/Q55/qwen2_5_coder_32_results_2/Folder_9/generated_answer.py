from itertools import cycle

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    cycled_lst = cycle(lst)
    for start in range(n):
        product = 1
        for i in range(n):
            product *= next(cycled_lst)
            if product == -36:
                result.append(lst[start:start + i + 1] if start + i + 1 <= n else lst[start:] + lst[:i + 1 - n + start])
    return result