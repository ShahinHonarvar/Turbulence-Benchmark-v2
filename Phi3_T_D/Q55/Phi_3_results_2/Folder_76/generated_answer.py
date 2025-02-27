from itertools import cycle, islice

def lists_with_product_equal_n(circular_list, n=247):
    circular_iter = cycle(circular_list)
    product = 1
    sublist = []
    result = []
    for value in circular_iter:
        product *= value
        sublist.append(value)
        if product == n:
            result.append(sublist[:])
            product = 1
            sublist.clear()
        for a in range(len(sublist), 0, -1):
            temp_product = 1
            for b in islice(sublist, a):
                temp_product *= b
            if temp_product == n:
                result.append(sublist[:a])
                break
        if len(sublist) > len(circular_list) or product == n:
            break
    return result