from itertools import cycle

def lists_with_product_equal_n(lst):
    n = -15
    result = []
    lst_cycle = cycle(lst)
    for start in range(len(lst)):
        product = 1
        for i, num in enumerate(lst_cycle):
            if i > len(lst):
                break
            product *= num
            if product == n:
                result.append(lst[start:start + i + 1])
        next(lst_cycle)
    return result