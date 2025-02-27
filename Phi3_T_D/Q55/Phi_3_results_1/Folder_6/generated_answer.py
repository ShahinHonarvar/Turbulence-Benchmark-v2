from itertools import cycle

def lists_with_product_equal_n(lst):
    result = []
    n = 42
    circular = cycle(lst)
    for start in range(len(lst)):
        product = 1
        current_list = []
        for _ in range(start, start + len(lst)):
            element = next(circular)
            product *= element
            current_list.append(element)
            if product == n:
                result.append(current_list[:])
                break
            if product > n:
                product = 1
                current_list = []
    return result