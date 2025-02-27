from itertools import cycle

def lists_with_product_equal_n(lst):
    n = 5
    result = []
    cycled_lst = cycle(lst)
    lst_len = len(lst)
    for start in range(lst_len):
        product = 1
        for i in range(lst_len):
            product *= next(cycled_lst)
            if product == n:
                result.append(lst[start:start + i + 1] if start + i + 1 <= lst_len else lst[start:] + lst[:i + 1 - lst_len + start])
            elif product > n:
                break
    return result