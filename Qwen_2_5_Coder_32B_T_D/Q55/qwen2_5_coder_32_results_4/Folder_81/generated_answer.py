from itertools import cycle

def lists_with_product_equal_n(lst):
    results = []
    n = len(lst)
    lst_cycled = cycle(lst)
    for start in range(n):
        current_product = 1
        for i in range(n):
            current_product *= next(lst_cycled)
            if current_product == -8:
                results.append(lst[start:start + i + 1] if start + i + 1 <= n else lst[start:] + lst[:i + 1 - start])
        lst_cycled = cycle(lst[start + 1:])
    return results