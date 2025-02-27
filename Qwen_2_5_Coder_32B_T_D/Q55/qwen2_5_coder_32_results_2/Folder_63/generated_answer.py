from itertools import cycle

def lists_with_product_equal_n(l):
    result = []
    n = len(l)
    cycled_l = cycle(l)
    for start in range(n):
        product = 1
        current_list = []
        for i in range(n):
            current = next(cycled_l)
            current_list.append(current)
            product *= current
            if product == 96:
                result.append(list(current_list))
            elif product > 96:
                break
        next(cycled_l, None)
    return result