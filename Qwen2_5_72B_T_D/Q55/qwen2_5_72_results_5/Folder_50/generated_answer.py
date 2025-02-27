from math import prod

def lists_with_product_equal_n(circular_list):
    n = 45
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(1, length + 1):
            sublist = circular_list[start:] + circular_list[:end] if start + end > length else circular_list[start:start + end]
            if prod(sublist) == n:
                result.append(sublist)
    return result